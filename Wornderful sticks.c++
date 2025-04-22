#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <algorithm>

using namespace std;

void solve() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        string s;
        cin >> s;

        int count_L = count(s.begin(), s.end(), '<');
        int count_R = count(s.begin(), s.end(), '>');

        vector<int> small, large;
        for (int i = 1; i <= count_L; i++) small.push_back(i);
        for (int i = n - count_R + 1; i <= n; i++) large.push_back(i);

        set<int> full_set;
        for (int i = 1; i <= n; i++) full_set.insert(i);
        for (int val : small) full_set.erase(val);
        for (int val : large) full_set.erase(val);

        int mid = *full_set.begin();

        vector<char> demands(n - 1);
        for (int i = 0; i < n - 1; i++) {
            demands[i] = (s[i] == '<') ? 'S' : 'L';
        }

        vector<int> ans(n);
        ans[0] = mid;
        int pos = 1;

        int i = 0;
        while (i < demands.size()) {
            char tag = demands[i];
            int j = i + 1;
            while (j < demands.size() && demands[j] == tag) j++;
            int length = j - i;

            if (tag == 'S') {
                vector<int> block(small.end() - length, small.end());
                small.resize(small.size() - length);
                sort(block.rbegin(), block.rend());
                for (int x : block) ans[pos++] = x;
            } else {
                vector<int> block(large.begin(), large.begin() + length);
                large.erase(large.begin(), large.begin() + length);
                sort(block.begin(), block.end());
                for (int x : block) ans[pos++] = x;
            }

            i = j;
        }

        for (int i = 0; i < n; i++) {
            cout << ans[i] << (i + 1 == n ? '\n' : ' ');
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}
