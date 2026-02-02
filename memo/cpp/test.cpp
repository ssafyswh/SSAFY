#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;
unordered_map<int, int> route(0);

int main() {
    int N, L;
    string command;
    cin >> N >> L >> command;
    int pos = 0;
    route[0] = 1;
    for (char d : command) {
        if (d == 'L') {
            pos--;
        } else {
            pos++;
        }
        route[pos]++;
    }
    
    return 0;
}