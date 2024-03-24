# coding=utf-8
import jieba

s = input("请输入一段中文文本，句子之间以逗号或句号分隔：")
slist = jieba.lcut(s)
m = 0
# 不需要使用字典进行名称和数量的统计，只需要统计个数即可
for i in slist:
    if i in "，。":
        continue
    else:
        m += 1
    # print(i, end="/")

print("\n中文词语数是：{}\n".format(m))

slist = s.split("，")
# 初始化一个空列表，用于存储输出结果
output_lines = []
for line in slist:
    # 去除末尾的句号
    line = line.strip("。")
    padding_spaces = (20 - len(line)) // 2
    # 注意这里的输出格式化字符串
    output_lines.append('{:{align}^{width}}'.format(line, align=' ', width=20))
print("\n".join(output_lines))
