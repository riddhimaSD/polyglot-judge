#include <bits/stdc++.h>
using namespace std;

string solve(const string& line) {
    istringstream in(line);
    int n, t; in >> n >> t;
    vector<int> a(n);
    for (auto& x : a) in >> x;
    int lo = 0, hi = n;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (a[mid] < t) lo = mid + 1; else hi = mid;
    }
    return to_string(lo);
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
