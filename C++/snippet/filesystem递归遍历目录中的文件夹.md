---
title: filesystem递归遍历目录中的文件夹  
date: 2023-03-03 10:39  
tags: [C++,filesystem]  
source: https://blog.csdn.net/tulingwangbo/article/details/116162340    
---

# filesystem递归遍历目录中的文件夹
```cpp
 
bool FindFilesInFolder(std::string strPath, std::vector<std::string> &vecFiles)
{
    char cEnd = *strPath.rbegin();
    if (cEnd == '\\' || cEnd == '/')
    {
        strPath = strPath.substr(0, strPath.length() - 1);
    }
 
    if (strPath.empty() || strPath == (".") || strPath == (".."))
        return false;
 
    std::error_code ec;
    std::filesystem::path fsPath(strPath);
    if (!std::filesystem::exists(strPath, ec)) {
        return false;
    }
    //  const std::string str1 = str.path().filename().string();
    //  std::cout << std::filesystem::absolute(str.path()) << '\n'; //绝对路径
    //  std::cout << std::filesystem::absolute(str.path()).string() << '\n';
    for (auto &itr : std::filesystem::directory_iterator(fsPath))
    {
        if (std::filesystem::is_directory(itr.status()))
        {
            FindFilesInFolder(itr.path().string(), vecFiles);
        }
        else
        {
            //if (std::regex_match(filename.string(), fileSuffix))
            //std::filesystem::remove_all(version_dir, ec);
            //std::filesystem::copy_file(from_file, to_file, std::filesystem::copy_options::skip_existing, ec))
            vecFiles.push_back(itr.path().string());
        }
    }
 
    return true;
}
```