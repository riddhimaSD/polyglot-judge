#include <bits/stdc++.h>
using namespace std;

string solve(const string& line) {
    istringstream in(line);
    int n; in >> n;
    long long best = 0, cur = 0, x;
    for (int i = 0; i < n; i++) { in >> x; cur = max(0LL, cur + x); best = max(best, cur); }
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
