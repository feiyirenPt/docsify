---
title: binary_fstream  
date: 2023-02-14 13:37  
tags:   
---

# binary_fstream

## 二进制读写文件
```cpp
void copy_binary_file(const std::string &s1, const std::string &s2) {
    std::ifstream ifs1(s1, std::ios::binary);
    std::ofstream ofs1(s2, std::ios::binary);
//获取文件大小
    ifs1.seekg(0, ifs1.end);
    std::streampos size = ifs1.tellg();
    ifs1.seekg(0, ifs1.beg);

    std::cout << size << std::endl;
    std::vector<char> szBuf(size);

    ifs1.read(&szBuf[0], size);
    ofs1.write(&szBuf[0], size);

```

## 重载左移右移运算符,让对象二进制串行化
```cpp
inline std::ostream &operator<<(std::ostream &os, const ProtoBuf &protoBuf) {
    (os << ProtoBuf::MethodToString(protoBuf.method) << " " << protoBuf.path
        << " " << protoBuf.size << " ")
        .write(&protoBuf.data[0], protoBuf.size);
    return os;
}

inline std::istream &operator>>(std::istream &is, ProtoBuf &protoBuf) {
    std::string method;
    std::filesystem::path path;
    int size;

    is >> method >> path >> size;

    is.ignore();
    std::cout << method << " " << path << " " << size << std::endl;
    std::vector<char> vec(size);
    is.read(&vec[0], size);

    protoBuf.SetMethod(ProtoBuf::StringToMethod(method));
    protoBuf.SetPath(path);
    protoBuf.SetData(vec);

    return is;
}
```