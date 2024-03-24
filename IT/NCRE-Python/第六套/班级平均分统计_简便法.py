# coding = utf-8

fi = open('data.txt', 'r')
d = {}
students = fi.readlines()
for i in students:
    i = i.strip().split(':')
    clas, score = i[1].split(',')
    # 字典d的key是str格式的班级名称，value是一个列表，列表中元素是该班级各同学的总分
    d[clas] = d.get(clas, []) + [eval(score)]

for i in d:
    # 这里i遍历的是字典d的key，即班级名称，sum的是字典的value（列表类型），即该班级各同学的总分
    # 注意d[i]是一个列表，所以要使用len()函数求列表长度
    avg_score = sum(d[i]) / len(d[i])
    # 平均分需要使用format()格式化输出，四舍五入到小数点后两位
    print('{}:{:.2f}'.format(i, avg_score))
