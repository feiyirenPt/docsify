# dijkstra

## 稠密图 普通dijkstra
```cpp
#define SIZE 10005
int n, m;
int g[SIZE][SIZE];

int dist[SIZE];
bool st[SIZE];

int dijkstra() {
    memset(dist, 0x3f, sizeof dist);
    dist[1] = 0;
    st[1] = true;
    for (int i = 1; i <= n; i++) {
        dist[i] = g[1][i];
    }

    for (int i = 1; i < n; i++) {
        int t = -1;
        for (int j = 1; j <= n; j++) {
            if (!st[j] && (t == -1 || dist[j] < dist[t])) {
                t = j;
            }
        }
        st[t] = true;
        for (int j = 1; j <= n; j++) {
            dist[j] = min(dist[j], g[t][j] + dist[t]);
        }
    }
    return dist[n] == 0x3f3f3f3f ? -1 : dist[n];
}

int main(int argc, char *argv[]) {
    freopen("data", "r", stdin);
    cin >> n >> m;
    memset(g, 0x3f, sizeof g);
    for (int i = 1; i <= m; i++) {
        int a, b, x;
        cin >> a >> b >> x;
        g[a][b] = min(g[a][b], x);
    }
    cout << dijkstra() << endl;

    return 0;
}
```

## 稠密图 堆优化dijkstra
```cpp
#define SIZE 10005
int n, m;
int g[SIZE][SIZE];

int dist[SIZE];
bool st[SIZE];
typedef pair<int, int> PII;

priority_queue<PII, std::vector<PII>, greater<PII>> heap;

int dijkstra() {
    memset(dist, 0x3f, sizeof dist);
    dist[1] = 0;

    heap.emplace(0, 1);

    while (heap.size()) {
        auto t = heap.top();
        heap.pop();
        cout << "pop {" << t.first << "," << t.second << "}" << endl;
        if (st[t.second]) continue;
        st[t.second] = true;
        for (int j = 1; j <= n; j++) {
            if (!st[j] && dist[j] > t.first + g[t.second][j]) {
                dist[j] = min(dist[j], t.first + g[t.second][j]);
                heap.emplace(dist[j], j);
                cout << "push {" << dist[j] << "," << j << "}" << endl;
            }
        }
    }

    return dist[n] == 0x3f3f3f3f ? -1 : dist[n];
}

int main(int argc, char *argv[]) {
    freopen("data", "r", stdin);
    cin >> n >> m;
    memset(g, 0x3f, sizeof g);
    for (int i = 1; i <= m; i++) {
        int a, b, x;
        cin >> a >> b >> x;
        g[a][b] = min(g[a][b], x);
    }
    cout << dijkstra() << endl;
    return 0;
}
```