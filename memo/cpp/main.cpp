#ifndef _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <stdio.h>

#define MAX_COM			1000
#define MAX_ONEFILE		50

extern void init(int N, int mSFileCnt[], int mSFileID[][MAX_ONEFILE], int mSFileSize[][MAX_ONEFILE]);
extern void makeNet(int K, int mComA[], int mComB[], int mDis[]);
extern void addLink(int mTime, int mComA, int mComB, int mDis);
extern void addShareFile(int mTime, int mComA, int mFileID, int mSize);
extern int downloadFile(int mTime, int mComA, int mFileID);
extern int getFileSize(int mTime, int mComA, int mFileID);

#define CMD_INIT		100
#define CMD_MAKENET		200
#define CMD_ADDLINK		300
#define CMD_SHARED		400
#define CMD_DOWNLOAD	500
#define CMD_GETSIZE		600

static int fileCnt[MAX_COM], fileID[MAX_COM][MAX_ONEFILE], fileSize[MAX_COM][MAX_ONEFILE];
static int comA[MAX_COM * 2], comB[MAX_COM * 2], Dis[MAX_COM * 2];

static bool run()
{
	int Q, N, K, time, id, size;
	int ret, ans;

	bool ok = false;

	scanf("%d", &Q);
	for (int q = 0; q < Q; q++)
	{
		int cmd;
		scanf("%d", &cmd);
		if (cmd == CMD_INIT)
		{
			scanf("%d", &N);
			for (int i = 0; i < N; i++) {
				scanf("%d", &fileCnt[i]);
				for (int k = 0; k < fileCnt[i]; k++) {
					scanf("%d %d", &fileID[i][k], &fileSize[i][k]);
				}
			}
			init(N, fileCnt, fileID, fileSize);
			ok = true;
		}
		else if (cmd == CMD_MAKENET)
		{
			scanf("%d", &K);
			for (int i = 0; i < K; i++) {
				scanf("%d %d %d", &comA[i], &comB[i], &Dis[i]);
			}
			makeNet(K, comA, comB, Dis);
		}
		else if (cmd == CMD_ADDLINK)
		{
			scanf("%d %d %d %d", &time, &comA[0], &comB[0], &Dis[0]);
			addLink(time, comA[0], comB[0], Dis[0]);
		}
		else if (cmd == CMD_SHARED)
		{
			scanf("%d %d %d %d", &time, &comA[0], &id, &size);
			addShareFile(time, comA[0], id, size);
		}
		else if (cmd == CMD_DOWNLOAD)
		{
			scanf("%d %d %d", &time, &comA[0], &id);
			ret = downloadFile(time, comA[0], id);
			scanf("%d", &ans);
			if (ans != ret) {
				ok = false;
			}
		}
		else if (cmd == CMD_GETSIZE)
		{
			scanf("%d %d %d", &time, &comA[0], &id);
			ret = getFileSize(time, comA[0], id);
			scanf("%d", &ans);
			if (ans != ret) {
				ok = false;
			}
		}
		else ok = false;
	}
	return ok;
}

int main()
{
	setbuf(stdout, NULL);
	freopen("sample_input.txt", "r", stdin);

	int T, MARK;
	scanf("%d %d", &T, &MARK);

	for (int tc = 1; tc <= T; tc++)
	{
		int score = run() ? MARK : 0;
		printf("#%d %d\n", tc, score);
	}

	return 0;
}