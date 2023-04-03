# dfs

## 排列数字

```cpp
void solve(int q[], int i) {
    if (i == n + 1) {
        for (int j = 1; j <= n; j++) {
            cout << q[j] << " ";
        }
        cout << endl;
        return;
    }
    for (int j = 1; j <= n; j++) {
        if (!used[j]) {
            used[j] = true;
            q[i] = j;
            solve(q, i + 1);
            used[j] = false;
        }
    }
}

int main(int argc, char *argv[]) {
    solve(q, 1);
    return 0;
}
```

## N皇后

```cpp
constexpr int n = 5;
#define SIZE 2 * n
int q[SIZE];
bool col[SIZE];
bool dg[SIZE];
bool udg[SIZE];

void solve(int q[], int x) {
    if (x == n + 1) {
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                cout << (q[i] == j ? 'Q' : '.');
            }
            cout << endl;
        }
        cout << endl;
        return;
    }
    for (int i = 1; i <= n; i++) {
        if (!col[i] && !dg[i - x + n] && !udg[i + x]) {
            col[i] = dg[i - x + n] = udg[i + x] = true;
            q[x] = i;
            solve(q, x + 1);
            col[i] = dg[i - x + n] = udg[i + x] = false;
        }
    }
}

int main(int argc, char *argv[]) {
    solve(q, 1);
    return 0;
}
```

## 树的重心
```cpp
#define N 10005
int n;

int h[N], e[N], ne[N], idx;
void add(int a, int b) {
    e[idx] = b;
    ne[idx] = h[a];
    h[a] = idx++;
}

bool vis[N];

int minn = 0x3f3f3f3f;

int solve(int x) {
    if (h[x] == -1) return 1;
    vis[x] = true;
    int cnt = 0;
    int size = 0;
    for (int j = h[x]; ~j; j = ne[j]) {
        if (!vis[j]) {
            int s = solve(j);
            size = max(size, s);
            cnt += s;
        }
    }
    int other = n - cnt;
    minn = min(minn, max(size, other));
    return cnt + 1;
}

int main(int argc, char *argv[]) {
    freopen("data", "r", stdin);
    cin >> n;
    int a, b;
    memset(h, -1, sizeof h);
    for (int i = 1; i < n; i++) {
        cin >> a >> b;
        add(a, b);
        add(b, a);
    }
    solve(1);
    cout << minn << endl;
    return 0;
}
```