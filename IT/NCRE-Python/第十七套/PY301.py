# PY301-1.py
# 请在.....处填写多行表达式或语句
# 可以修改其他代码

def ravg(lst):
    """
    计算给定列表的平均值，并四舍五入到小数点后一位。
    参数:
    lst - 一个包含数字的列表。
    返回值:
    返回计算得到的平均值，四舍五入到小数点后一位。
    """
    sum = 0  # 初始化总和为0
    for i in lst:
        sum += i  # 遍历列表，累加元素值
    return round(sum / len(lst), 1)  # 计算平均值并四舍五入到小数点后一位



qzlst = []
swlst = []
zylst = []
with open("data2.csv", "r") as f:
    datas = f.readlines()
    for i in datas:
        if i in datas[:5]:
            print(i, end='')
        if i in datas[1:]:
            ls = i.strip().split(',')
            qzlst.append(eval(ls[1]))
            swlst.append(eval(ls[2]))
            zylst.append(eval(ls[3]))
avglst = ["平均值", ravg(qzlst), ravg(swlst), ravg(zylst)]
maxlst = ["最大值", max(qzlst), max(swlst), max(zylst)]
minlst = ["最小值", min(qzlst), min(swlst), min(zylst)]

with open("tongji.csv", "w") as f:
    f.write('统计,报名,弃考,有效\n')
    # *用于 unpacking（解包）参数
    # 它允许你将一个列表或元组的元素作为单独的参数传递给函数
    f.write('{},{},{},{}'.format(*avglst) + '\n')
    f.write('{},{},{},{}'.format(*maxlst) + '\n')
    f.write('{},{},{},{}'.format(*minlst))
