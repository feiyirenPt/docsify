import os


def dirList(f, path, space):
    filelist = os.listdir(path)
    for filename in filelist:
        filepath = os.path.join(path, filename)
        space += 4
        if os.path.isdir(filepath):
            f.write(" "*space + "- **"+os.path.basename(filepath)+"**\n")
            dirList(f, filepath, space)
        else:
            filename = os.path.basename(filepath)
            if not filename.startswith("_") and not filename.startswith(".") and filename.endswith(".md"):
                f.write(" "*space +
                        "- ["+os.path.basename(filepath)+"](" + filepath + ")\n")
        space -= 4


with open("_sidebar.md", "w", encoding='UTF-8') as f:
    dirList(f, '.', -4)
