# bellmanfold


## 有边数限制的最短路(带负边，带环最短路 or 判断负环)
```cpp
#define SIZE 10005
int n, m, k;
int dist[SIZE];

struct Edge {
    int a, b, w;
    friend istream& operator>>(istream& is, Edge& e) {
        is >> e.a >> e.b >> e.w;
        return is;
    }

    friend ostream& operator<<(ostream& os, Edge& e) {
        os << "[" << e.a << "," << e.b << "," << e.w << "]";
        return os;
    }
} edge[SIZE];

int bellmanfold() {
    memset(dist, 0x3f, sizeof dist);
    dist[1] = 0;

    for (int i = 1; i <= k; i++) {
        int backup[SIZE];
        memcpy(backup, dist, sizeof(int) * n);
        for (int j = 1; j <= m; j++) {
            int a = edge[j].a;
            int b = edge[j].b;
            int w = edge[j].w;
            dist[b] = min(dist[b], backup[a] + w);
        }
    }
    return dist[n] > 0x3f3f3f3f / 2 ? -1 : dist[n];
}

int main(int argc, char* argv[]) {
    freopen("data", "r", stdin);
    cin >> n >> m >> k;
    for (int i = 1; i <= m; i++) {
        cin >> edge[i];
    }
    cout << bellmanfold() << endl;
    return 0;
}
```