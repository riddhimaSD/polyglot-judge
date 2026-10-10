#include <bits/stdc++.h>
using namespace std;

string solve(const string& line) {
    istringstream in(line);
    int n; in >> n;
    int best, cur, x;
    in >> best; cur = best;
    for (int i = 1; i < n; i++) { in >> x; cur = max(x, cur + x); best = max(best, cur); }
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
