#include <bits/stdc++.h>
using namespace std;

vector<int> tmpv;
long long sortc(vector<int>& a, int lo, int hi) {
    if (hi - lo <= 1) return 0;
    int m = (lo + hi) / 2;
    long long c = sortc(a, lo, m) + sortc(a, m, hi);
    int i = lo, j = m, k = lo;
    while (i < m && j < hi) {
        if (a[i] <= a[j]) tmpv[k++] = a[i++];
        else { tmpv[k++] = a[j++]; c += m - i; }
    }
    while (i < m) tmpv[k++] = a[i++];
    while (j < hi) tmpv[k++] = a[j++];
    for (int p = lo; p < hi; p++) a[p] = tmpv[p];
    return c;
}
string solve(const string& line) {
    istringstream in(line);
    int n; in >> n;
    vector<int> a(n);
    for (auto& x : a) in >> x;
    tmpv.assign(n, 0);
    return to_string(sortc(a, 0, n));
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
