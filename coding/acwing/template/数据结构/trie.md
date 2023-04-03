# trie

## trie
```cpp
const int N = 300;

int son[N][26];
int cnt[N];
int idx;

void insert(string s) {
    int p = 0;
    for (int i = 0; i < s.size(); i++) {
        if (!son[p][s[i]-'a']) {
            son[p][s[i]-'a'] = ++idx;
        }
        p = son[p][s[i]-'a'];
    }
	cnt[p]++;
}
int query(string s){
	int p = 0;
	for(int i = 0;i<s.size();i++){
		if(!son[p][s[i]-'a']) return -1;
		p = son[p][s[i]-'a'];
	}
	return cnt[p];
}

int main(int argc, char *argv[]) { 
	insert("abc");
	cout << query("abc");
	return 0; 
}
```

## 最大异或对
```cpp

int n;
int q[10005];

int son[10005][2];
#include <bitset>

int idx;

void insert(int x) {
    int p = 0;
    for (int i = 30; ~i; i--) {
        int &u = son[p][x >> i & 1];
        if (!u) u = ++idx;
        p = u;
    }
}

int query(int x) {
    int p = 0;
    int res = 0;
    for (int i = 30; ~i; i--) {
        int s = x >> i & 1;
        if (son[p][!s]) {
            res += 1 << i;
            p = son[p][!s];
        } else
            p = son[p][s];
    }
    return res;
}

int main(int argc, char *argv[]) {
    freopen("data", "r", stdin);
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> q[i];
        insert(q[i]);
    }

    for (int i = 0; i < n; i++) {
        cout << bitset<10>(query(q[i])).to_string() << endl;
    }

    return 0;
}
```