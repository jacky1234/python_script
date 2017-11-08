import os

# todo 修改文件指定内容
directory = input("请输入你要扫描的目录或者文件:")
origin = input("修改前的内容:")
des = input("修改后的内容:")

modify = []
result = []
modifying_path = ''


def modify_all(dir):
    try:
        if os.path.isdir(dir):
            get_dir = os.listdir(dir)
            for i in get_dir:
                sub_dir = os.path.join(dir, i)
                if os.path.isdir(sub_dir):  # 如果当前仍然是文件夹，递归调用
                    modify_all(sub_dir)
                else:
                    modify_file(sub_dir)
        else:
            modify_file(dir)
    except Exception as exc:
        print(exc + ",current path :" + modifying_path)


def modify_file(path):
    fp = open(path, "r")
    for line in fp.readlines():
        if line.find(origin) != 0:
            result.append(line)
        if path not in modify:
            modify.append(path)


try:
    print("替换 ing....")
    modify_all(directory)
    print("替换 done....result:")
    for i in modify:
        print(i+"：")
        for j in result:
            print(j)
except OSError:
    print("替换 错误....")
