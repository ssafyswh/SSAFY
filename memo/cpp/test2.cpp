#include <iostream>
#include <vector>

using namespace std;

int main () {
    vector<int> chess = {1, 1, 2, 2, 2, 8};
    for (int i = 0; i < 6; i++) {
        int num;
        cin >> num;
        cout << chess[i] - num << ' ';
    }
    return 0;
}