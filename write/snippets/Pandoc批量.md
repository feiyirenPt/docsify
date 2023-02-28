---
title: Pandoc实现批量将md文件转换为其它文件
date: 2023-02-24 09:47  
tags: [pandoc]  
source: https://zhuanlan.zhihu.com/p/145787589  
---

```py
import os


def get_file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):  # 获取当前文件夹的信息
        # print(root)
        # print(dirs)
        # print(files)
        for file in files:                       # 扫描所有文件
            if os.path.splitext(file)[1] == ".md":# 提取出所有后缀名为md的文件
                # print(root)
                os.chdir(root)

                print("转换开始：" + "pandoc " + file + " -o " + os.path.splitext(file)[0] + ".docx")
                # 使用os.system调用pandoc进行格式转化
                os.system("pandoc " + file + " -o " + os.path.splitext(file)[0] + ".docx")
                print("转换完成...")


if __name__ == "__main__":
    get_file_name(r"C:\Users\Administrator\Desktop\其它")  # 修改文件路径
```