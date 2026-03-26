#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <queue>

using namespace std;

#define MAX_COM 1005
const int INF = 1e8;

int N_coms;
int dist_mat[MAX_COM][MAX_COM];

unordered_map<int, int> file_sizes;
unordered_map<int, vector<int>> source_locs;
unordered_set<int> is_source[MAX_COM];

struct Request {
    int com;
    int f_id;
    long long downloaded;
    int last_time;
    int sources;
    bool done;
};

vector<Request> reqs;
vector<int> active_reqs;
unordered_map<int, int> req_map[MAX_COM];

int calc_sources(int com, int f_id) {
    int cnt = 0;
    if (source_locs.find(f_id) != source_locs.end()) {
        for (int src : source_locs[f_id]) {
            if (dist_mat[com][src] <= 5000) cnt++;
        }
    }
    return cnt;
}

void flush_req(int r_idx, int mTime) {
    if (reqs[r_idx].done) return;
    long long duration = mTime - reqs[r_idx].last_time;
    if (duration > 0 && reqs[r_idx].sources > 0) {
        reqs[r_idx].downloaded += duration * reqs[r_idx].sources * 9;
        if (reqs[r_idx].downloaded >= file_sizes[reqs[r_idx].f_id]) {
            reqs[r_idx].downloaded = file_sizes[reqs[r_idx].f_id];
            reqs[r_idx].done = true;
        }
    }
    reqs[r_idx].last_time = mTime;
}

void init(int N, int mShareFileCnt[], int mFileID[][50], int mFileSize[][50]) {
    N_coms = N;
    file_sizes.clear();
    source_locs.clear();
    reqs.clear();
    active_reqs.clear();
    
    for (int i = 0; i < MAX_COM; ++i) {
        req_map[i].clear();
        is_source[i].clear();
        for (int j = 0; j < MAX_COM; ++j) dist_mat[i][j] = (i == j) ? 0 : INF;
    }

    for (int i = 0; i < N; ++i) {
        int com = i + 1;
        for (int k = 0; k < mShareFileCnt[i]; ++k) {
            int f_id = mFileID[i][k];
            file_sizes[f_id] = mFileSize[i][k];
            source_locs[f_id].push_back(com);
            is_source[com].insert(f_id);
        }
    }
}

void makeNet(int K, int mComA[], int mComB[], int mDis[]) {
    vector<pair<int, int>> adj[MAX_COM];
    for (int i = 0; i < K; ++i) {
        adj[mComA[i]].push_back({mComB[i], mDis[i]});
        adj[mComB[i]].push_back({mComA[i], mDis[i]});
    }
    for (int i = 1; i <= N_coms; ++i) {
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        pq.push({0, i});
        dist_mat[i][i] = 0;
        
        while (!pq.empty()) {
            int d = pq.top().first;
            int u = pq.top().second;
            pq.pop();
            
            if (d > dist_mat[i][u]) continue;
            
            for (auto& edge : adj[u]) {
                if (dist_mat[i][edge.first] > d + edge.second) {
                    dist_mat[i][edge.first] = d + edge.second;
                    pq.push({dist_mat[i][edge.first], edge.first});
                }
            }
        }
    }
}

void addLink(int mTime, int mComA, int mComB, int mDis) {
    if (mDis >= dist_mat[mComA][mComB]) return;
    for (int i = 0; i < (int)active_reqs.size(); ) {
        int r_idx = active_reqs[i];
        flush_req(r_idx, mTime);
        if (reqs[r_idx].done) {
            active_reqs[i] = active_reqs.back();
            active_reqs.pop_back();
        } else {
            ++i;
        }
    }

    vector<int> uA, uB;
    for (int i = 1; i <= N_coms; ++i) {
        if (dist_mat[i][mComA] + mDis < dist_mat[i][mComB]) uA.push_back(i);
        if (dist_mat[i][mComB] + mDis < dist_mat[i][mComA]) uB.push_back(i);
    }
    dist_mat[mComA][mComB] = dist_mat[mComB][mComA] = mDis;
    for (int i : uA) {
        for (int j : uB) {
            int new_d = dist_mat[i][mComA] + mDis + dist_mat[mComB][j];
            if (new_d < dist_mat[i][j]) {
                dist_mat[i][j] = dist_mat[j][i] = new_d;
            }
        }
    }

    for (int r_idx : active_reqs) {
        reqs[r_idx].sources = calc_sources(reqs[r_idx].com, reqs[r_idx].f_id);
    }
}

void addShareFile(int mTime, int mComA, int mFileID, int mSize) {
    if (file_sizes.find(mFileID) == file_sizes.end()) {
        file_sizes[mFileID] = mSize;
    }
    
    if (is_source[mComA].find(mFileID) == is_source[mComA].end()) {
        is_source[mComA].insert(mFileID);
        source_locs[mFileID].push_back(mComA);
        
        for (int i = 0; i < (int)active_reqs.size(); ) {
            int r_idx = active_reqs[i];
            if (reqs[r_idx].f_id == mFileID) {
                flush_req(r_idx, mTime);
                if (reqs[r_idx].done) {
                    active_reqs[i] = active_reqs.back();
                    active_reqs.pop_back();
                    continue;
                }
                if (dist_mat[reqs[r_idx].com][mComA] <= 5000) {
                    reqs[r_idx].sources++;
                }
            }
            ++i;
        }
    }
}

int downloadFile(int mTime, int mComA, int mFileID) {
    if (req_map[mComA].find(mFileID) != req_map[mComA].end()) {
        int r_idx = req_map[mComA][mFileID];
        flush_req(r_idx, mTime);
        return calc_sources(mComA, mFileID);
    }

    int sc = calc_sources(mComA, mFileID);
    
    Request r;
    r.com = mComA;
    r.f_id = mFileID;
    r.downloaded = 0;
    r.last_time = mTime;
    r.sources = sc;
    r.done = false;
    
    reqs.push_back(r);
    int r_idx = (int)reqs.size() - 1;
    req_map[mComA][mFileID] = r_idx;
    active_reqs.push_back(r_idx);
    
    return sc;
}

int getFileSize(int mTime, int mComA, int mFileID) {
    if (is_source[mComA].count(mFileID)) return file_sizes[mFileID];
    
    if (req_map[mComA].find(mFileID) != req_map[mComA].end()) {
        int r_idx = req_map[mComA][mFileID];
        flush_req(r_idx, mTime);
        return (int)reqs[r_idx].downloaded;
    }
    return 0;
}