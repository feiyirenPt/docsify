---
title: gitlab api
date: 2023-02-02 14:34  
tags: [gitlab,api]  
---

### json格式化

```python
result = json.dumps(json.loads(res.text), indent=4)
```

### 参数配置
```python
headers = {
    "Private-Token": "<Your-Token>",
}
params = {
    "branch": "master",
    "commit_message": "test",
    ...
}
```

### query
```python
res = requests.get("https://gitcode.net/api/v4/projects/:id/repository/tree")
```

### create
```python
res = requests.post("https://gitcode.net/api/v4/projects/:id/repository/files/:file",headers=headers,data=params)
```

### delete
```python
res = requests.delete("https://gitcode.net/api/v4/projects/:id/repository/files/:file",headers=headers,data=params)
```
- :id 项目id
- :file 文件路径,中间的 `/` 用 `%2F` 替换

