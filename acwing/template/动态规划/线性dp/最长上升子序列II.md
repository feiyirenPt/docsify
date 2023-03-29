```cpp
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;
const int N = 1e5;

int q[N], f[N];
int n;

int main(int argc, char *argv[]) {
    freopen("data", "r", stdin);
    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> q[i];
    }
    vector<int> vec;
    vec.push_back(q[1]);
    for (int i = 1; i <= n; i++) {
        auto j = q[i];
        if (vec.back() < j)
            vec.push_back(j);
        else
            *lower_bound(vec.begin(), vec.end(), j) = j;
    }
    cout << vec.size() << endl;

    return 0;
}
```