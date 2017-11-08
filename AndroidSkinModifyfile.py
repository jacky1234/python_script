import os

dir = input("请输入你要扫描的目录或者文件:")
modify = []
remove = []

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

    print("modify:")
    for m in modify:
        print(m)
    print("remove:")
    for r in remove:
        print(r)

    print("success!")
except OSError:
    print("exception!")
