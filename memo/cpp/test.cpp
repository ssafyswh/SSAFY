#include <iostream>
#include <string>

using namespace std;

string replaceAll(string str, const string &from, const string &to)
{
    if (from.empty())
        return str;
    size_t start_pos = 0;
    while ((start_pos = str.find(from, start_pos)) != string::npos)
    {
        str.replace(start_pos, from.length(), to);
        start_pos += to.length();
    }
    return str;
}

int main()
{
    int T;
    cin >> T;
    for (int t = 0; t < T; t++)
    {
        string s, p;
        cin >> s >> p;
        replaceAll(s, p, "s");
        cout << s.length() << "\n";
    }
    return 0;
}