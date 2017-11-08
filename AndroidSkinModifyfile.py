import os
import shutil

dir = input("请输入你要扫描的目录或者文件:")
modify = []
remove = []
error = []
exeFiles = []
exe9Dir = "9Path"

try:
    for f in os.listdir(dir):
        if f.find("@2x.png") > 0:
            path = os.path.join(dir, f)
            remove.append(path)
            os.remove(path)
        if f.find("@3x.png") > 0:
            # 源文件名字
            oldName = f
            newName = f.replace("@3x.png", ".png")
            modify.append(oldName + "->" + newName)
            os.rename(os.path.join(dir, oldName), os.path.join(dir, newName))
        if f.find(" ") > 0:
            error.append(f)
        if f.find(".9.png") > 0:
            exeFiles.append(f)

    # delete dir if exist
    if os.path.exists(os.path.join(dir, exe9Dir)):
        shutil.rmtree(os.path.join(dir, exe9Dir))
    os.makedirs(os.path.join(dir, exe9Dir))

    print("copy .9 file to " + exe9Dir)
    for f in exeFiles:
        shutil.copy(os.path.join(dir, f), os.path.join(dir, exe9Dir, f))

    print("modify:")
    for m in modify:
        print(m)

    print("remove:")
    for r in remove:
        print(r)

    print("error contain blank file list:")
    for e in error:
        print(e)

    print("success!")
except OSError as error:
    print("exception!:", error)
