#include <bits/stdc++.h>
using namespace std;

string solve(const string& line) {
    istringstream in(line);
    int n; in >> n;
    vector<int> a(n);
    for (auto& x : a) in >> x;
    long long c = 0;
    for (int i = 0; i < n; i++) for (int j = i + 1; j < n; j++) if (a[i] > a[j]) c++;
    return to_string(c);
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
