# bfs

## 走迷宫

```cpp
typedef pair<int, int> PII;

#define SIZE 105
int n, m;
int maze[SIZE][SIZE];
int cnt[SIZE][SIZE];

int x[4] = {-1, 0, 1, 0};
int y[4] = {0, -1, 0, 1};

int main(int argc, char *argv[]) {
    freopen("data", "r", stdin);
    cin >> n >> m;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            cin >> maze[i][j];
            cout << maze[i][j] << " ";
        }
        cout << endl;
    }
    queue<PII> q;
    q.emplace(1, 1);
    while (!q.empty()) {
        auto t = q.front();
        q.pop();
        maze[t.first][t.second] = 1;
        for (int i = 0; i < 4; i++) {
            PII next{t.first + x[i], t.second + y[i]};
            if (next.first > 0 && next.first <= n && next.second > 0 &&
                next.second <= m && !maze[next.first][next.second]) {
                q.push(next);
                cnt[next.first][next.second] = cnt[t.first][t.second] + 1;
            }
        }
    }

    cout << cnt[n][m] << endl;

    return 0;
}
```

## 图中点的层次
```cpp
#define N 10005
int n, m;

int h[N], e[N], ne[N], idx;

bool vis[N];
int dist[N];

void add(int a, int b) {
    cout << "add " << a << " " << b << endl;
    e[idx] = b;
    ne[idx] = h[a];
    h[a] = idx++;
}

void solve() {
    queue<int> q;
    q.push(1);
    while (q.size()) {
        auto f = q.front();
        q.pop();
        cout << "pop " << f << endl;
        for (int j = h[f]; ~j; j = ne[j]) {
            if (!vis[e[j]]) {
                q.push(e[j]);
                dist[e[j]] = dist[f] + 1;
                vis[e[j]] = true;
                cout << "push " << e[j] << endl;
            }
        }
    }
}

int main(int argc, char *argv[]) {
    freopen("data", "r", stdin);
    cin >> n >> m;
    memset(h, -1, sizeof h);
    for (int i = 1; i <= m; i++) {
        int a, b;
        cin >> a >> b;
        add(a, b);
    }
    solve();
    for (int i = 1; i <= n; i++) {
        cout << dist[i] << " ";
    }
    return 0;
}
```