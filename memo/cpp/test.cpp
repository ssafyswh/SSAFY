#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int R, C, T;

vector<pair<int, int>> delta = {
    {0, 1},
    {1, 0},
    {0, -1},
    {-1, 0},
};

bool check(int r, int c) {
    if (r < 0 || r >= R) return false;
    if (c < 0 || c >= C) return false;
    return true;
}

vector<vector<int>> room;

void spread_dust(int r, int c, int dust) {
    int spread = dust / 5;
    for (pair<int ,int> d : delta) {
        int nr = r + d.first, nc = c + d.second;
        if (check(nr, nc) && room[nr][nc] != -1) {
            room[nr][nc] += spread;
        }
    }
}

void purify(int sr, int sc, bool is_clockwise) {
    if (is_clockwise) {
        room[sr + 1][sc] = 0;
        for (int r = sr + 1; r < R - 2; r++) {
            swap(room[r][sc], room[r + 1][sc]);
        }
        for (int c = sc + 1; c < C - 2; c++) {
            swap(room[R - 1][c], room[R - 1][c + 1]);
        }
        for (int r = R - 1; r > sr; r--) {
            swap(room[r][C - 1], room[r - 1][C - 1]);
        }
        for (int c = C - 1; c > sc + 1; c--) {
            swap(room[c][sr], room[c - 1][sr]);
        }
    }
    else {
        room[sr - 1][sc] = 0;
        for (int r = sr - 1; r < 1; r--) {
            swap(room[r][sc], room[r + 1][sc]);
        }
        for (int c = sc - 1; c < C - 2; c++) {
            swap(room[R - 1][c], room[R - 1][c + 1]);
        }
        for (int r = R - 1; r > sr; r++) {
            swap(room[r][C - 1], room[r - 1][C - 1]);
        }
        for (int c = C - 1; c > sc + 1; c++) {
            swap(room[c][sr], room[c - 1][sr]);
        }
    }
}

void purify2() {

}

int main() {
    cin >> R >> C >> T;
    for (int y = 0; y < R; y++) {
        room.push_back(vector<int> {});
        for (int x = 0; x < C; x++) {
            int dust;
            cin >> dust;
            room[y].push_back(dust);
        }
    }
    return 0;
}