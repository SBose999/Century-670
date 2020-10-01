#include <bits/stdc++.h>

#define int long long
using namespace std;

void solve() {
    int n;
    cin >> n;
    vector<int> v1, v2;
    unordered_map<int, int> f;
    for (int i = 0, t; i < n; i++) {
        cin >> t;
        f[t]++;
    }
    for (auto &i : f) {
        if (v1.empty()) {
            if (i.first - 0 != 0)
                break;
            v1.emplace_back(i.first);
            i.second--;
        } else {
            if (i.first - v1.back() == 1) {
                v1.emplace_back(i.first);
                i.second--;
            } else {
                break;
            }
        }
    }
    for (auto &i : f) {
        if (v2.empty()) {
            if (!i.second or i.first - 0 != 0)
                break;
            v2.emplace_back(i.first);
            i.second--;
        } else {
            if (i.second and i.first - v2.back() == 1) {
                v2.emplace_back(i.first);
                i.second--;
            } else {
                continue;
            }
        }
    }
    cout << (v1.empty() ? 0 : v1.back() + 1) + (v2.empty() ? 0 : v2.back() + 1) << '\n';
}

signed main() {
    int t;
    cin >> t;
    while (t--)
        solve();
    return 0;
}
