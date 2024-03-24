# coding=utf-8
fi = open("data.txt", "r", encoding="GBK")
[name, score] = [0, 0]

for line in fi:
    if int(line[-4:]) > score:
        name = line[:3]
        print(line)
        # 下面是-4，表示从倒数第4个字符开始，到文件末尾，末尾还有一个\n，所以是-4
        score = int(line[-4:])
    else:
        continue

print("{}:{}".format(name, score))
