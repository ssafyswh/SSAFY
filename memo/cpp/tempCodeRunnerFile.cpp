#include <iostream>
#include <string>

using namespace std;

int main() {
    int N;
    cin >> N;
    while (N--) {
        int ord;
        string text;
        cin >> ord >> text;
        string result = "";
        for (int i = 0; i < text.size(); i++) {
            if (i == ord - 1) continue;
            result += text[i];
        }
        cout << result << "\n";
    }
    return 0;
}