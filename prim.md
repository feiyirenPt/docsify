# prim

```cpp
#define N 505
#define M 10005

int n, m;
int h[N], e[M], ne[M], w[N], idx;
int dist[N];
bool vis[N];

void add(int a, int b, int x) {
    e[idx] = b, ne[idx] = h[a], w[idx] = x, h[a] = idx++;
}

int prim() {
    memset(dist, 0x3f, sizeof dist);
    dist[1] = 0;
    int ret = 0;
    for (int i = 1; i <= n; i++) {
        int t = -1;
        for (int j = 1; j <= n; j++) {
            if (!vis[j] && (t == -1 || dist[t] > dist[j])) {
                t = j;
            }
        }
        if (t == 0x3f3f3f3f) return -1;
        vis[t] = true;
        ret += dist[t];
        for (int j = h[t]; ~j; j = ne[j]) {
            auto p = e[j];
            dist[p] = min(dist[p], w[j]);
        }
    }
    return ret;
}

int main(int argc, char *argv[]) {
    freopen("data", "r", stdin);
    cin >> n >> m;
    memset(h, -1, sizeof h);
    for (int i = 1; i <= m; i++) {
        int a, b, m;
        cin >> a >> b >> m;
        add(a, b, m);
        add(b, a, m);
    }

    cout << prim() << endl;

    return 0;
}
```