```cpp
#define SIZE 10005
int n, m, k;
int g[SIZE][SIZE];

void floyd() {
    for (int k = 1; k <= n; k++) {
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                g[i][j] = min(g[i][j], g[i][k] + g[k][j]);
            }
        }
    }
}

int main(int argc, char *argv[]) {
    freopen("data", "r", stdin);
    cin >> n >> m >> k;
    memset(g, 0x3f, sizeof g);
    for (int i = 1; i <= m; i++) {
        int a, b, w;
        cin >> a >> b >> w;
        g[a][b] = min(g[a][b], w);
    }

    while (k--) {
        int a, b;
        cin >> a >> b;
        cout << (g[a][b] == 0x3f3f3f3f ? -1 : g[a][b]) << endl;
    }

    return 0;
}
```