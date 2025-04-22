#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void solve() {
    int t;
    cin >> t;

    while (t--) {
        int n, k;
        cin >> n >> k;

        vector<int> l(n), r(n);
        for (int i = 0; i < n; ++i) cin >> l[i];
        for (int i = 0; i < n; ++i) cin >> r[i];

        long long S = 0;
        vector<int> extras(n);

        for (int i = 0; i < n; ++i) {
            if (l[i] >= r[i]) {
                S += l[i];
                extras[i] = r[i];
            } else {
                S += r[i];
                extras[i] = l[i];
            }
        }

        sort(extras.rbegin(), extras.rend()); // Sort descending
        long long overflow_needed = 0;
        for (int i = 0; i < k - 1 && i < n; ++i) {
            overflow_needed += extras[i];
        }

        long long x_min = S + overflow_needed + 1;
        cout << x_min << endl;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();
    return 0;
}
