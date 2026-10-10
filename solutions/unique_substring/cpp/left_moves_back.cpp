#include <bits/stdc++.h>
using namespace std;

string solve(const string& line) {
    string s = line;
    while (!s.empty() && (s.back() == '\r' || s.back() == ' ')) s.pop_back();
    vector<int> last(128, -1);
    int left = 0, best = 0;
    for (int i = 0; i < (int)s.size(); i++) {
        int c = s[i];
        if (last[c] >= 0) left = last[c] + 1;
        last[c] = i;
        best = max(best, i - left + 1);
    }
    return to_string(best);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string line;
    getline(cin, line);
    int t = stoi(line);
    for (int i = 0; i < t; i++) {
        getline(cin, line);
        cout << solve(line) << "\n";
    }
}
