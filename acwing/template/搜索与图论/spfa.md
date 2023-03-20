```cpp
#define N 10005
int n, m;

int h[N], e[N], ne[N], w[N], idx;
bool st[N];
int dist[N];

void add(int a, int b, int x) {
    e[idx] = b, ne[idx] = h[a], w[idx] = x, h[a] = idx++;
}

int spfa() {
    memset(dist, 0x3f, sizeof dist);
    dist[1] = 0;

    queue<int> q;
    q.push(1);
    st[1] = true;
    while (q.size()) {
        auto t = q.front();
        q.pop();
        st[t] = false;
        for (int j = h[t]; ~j; j = ne[j]) {
            auto p = e[j];
            if (dist[p] > dist[t] + w[j]) {
                dist[p] = dist[t] + w[j];
                q.push(p);
                st[p] = true;
            }
        }
    }
    return dist[n] == 0x3f3f3f3f ? -1 : dist[n];
}

int main(int argc, char *argv[]) {
    freopen("data", "r", stdin);
    cin >> n >> m;

    memset(h, -1, sizeof h);

    for (int i = 1; i <= m; i++) {
        int a, b, w;
        cin >> a >> b >> w;
        add(a, b, w);
    }
    cout << spfa() << endl;

    return 0;
}
```