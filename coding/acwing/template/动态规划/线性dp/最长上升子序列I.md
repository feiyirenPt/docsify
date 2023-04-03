```cpp
#include <algorithm>
#include <iostream>

using namespace std;
const int N = 1e5 + 5;
int q[N];
int n;
int a[N];

int main(int argc, char *argv[]) {
    freopen("data", "r", stdin);
    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> q[i];
        a[i] = 1;
    }
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j < i; j++) {
            if (q[i] > q[j]) a[i] = max(a[i], a[j] + 1);
        }
    }
    cout << *max_element(begin(a), end(a)) << endl;
    return 0;
}
```