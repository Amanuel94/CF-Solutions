#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
#include <map>
#include <tuple>

using namespace std;

#define inf INT_MAX
#define ii() read_int()
#define li() read_pair()

typedef tuple<int, int, int> Song;

int read_int() {
    int x;
    cin >> x;
    return x;
}

pair<int, int> read_pair() {
    int a, b;
    cin >> a >> b;
    return {a, b};
}

void ms(int l, int r, vector<Song>& arr, vector<int>& res) {
    if (l > r) return;
    if (l == r) return;

    int m = (l + r) / 2;

    ms(l, m, arr, res);
    ms(m + 1, r, arr, res);

    vector<Song> left(arr.begin() + l, arr.begin() + m + 1);
    vector<Song> right(arr.begin() + m + 1, arr.begin() + r + 1);

    vector<Song> merged;
    size_t li = 0, ri = 0;

    while (li < left.size() && ri < right.size()) {
        if (get<1>(left[li]) >= get<1>(right[ri])) {
            merged.push_back(right[ri]);
            res[get<2>(right[ri])] = min(res[get<2>(right[ri])], get<1>(left[li]));
            ri++;
        } else {
            merged.push_back(left[li]);
            li++;
        }
    }

    while (li < left.size()) {
        merged.push_back(left[li]);
        li++;
    }

    while (ri < right.size()) {
        merged.push_back(right[ri]);
        ri++;
    }

    for (size_t i = 0; i < merged.size(); i++) {
        arr[l + i] = merged[i];
    }
}

int main() {
    int t = ii();
    while (t--) {
        int n = ii();
        vector<Song> sngs;
        vector<Song> sngsc;
        map<pair<int, int>, int> cnt;

        for (int i = 0; i < n; i++) {
            auto p = li();
            sngs.push_back({p.first, p.second, i});
            sngsc.push_back(sngs.back());
            cnt[{p.first, p.second}]++;
        }

        vector<int> lres(n, inf), rres(n, inf);

        sort(sngs.begin(), sngs.end(), [](const Song& a, const Song& b) {
            return make_pair(get<0>(a), -get<1>(a)) < make_pair(get<0>(b), -get<1>(b));
        });

        ms(0, n - 1, sngs, rres);

        for (auto& song : sngs) {
            song = {-get<1>(song), -get<0>(song), get<2>(song)};
        }

        sort(sngs.begin(), sngs.end(), [](const Song& a, const Song& b) {
            return make_pair(get<0>(a), -get<1>(a)) < make_pair(get<0>(b), -get<1>(b));
        });

        ms(0, n - 1, sngs, lres);

        for (int i = 0; i < n; i++) {
            if (cnt[{get<0>(sngsc[i]), get<1>(sngsc[i])}] >= 2) {
                cout << 0 << endl;
                continue;
            }

            int lf = -lres[i], rf = rres[i];
            if (lf == -inf || rf == inf) {
                cout << 0 << endl;
            } else {
                cout << get<0>(sngsc[i]) - lf + rf - get<1>(sngsc[i]) << endl;
            }
        }
    }

    return 0;
}
