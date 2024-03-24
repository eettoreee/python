# 字符串使用演示
from idlelib.multicall import r

name = '叶宜涛'
school = "北京市陈经纶中学"

# \n 的作用是换行显示
print('我是{0}，\n我来自{1}'.format(name, school))

# 或者
print('''大家好，
我是{0}，
我来自{1}'''.format(name, school))

# 在python中，\通常表示转义，使字符失去原有的意义
print("我来自北京市\"怀柔区\"")  # 此处演示不应使用单引号

# \前加上r时候，\失去转义的作用
print('北京市' + r'\n' + '怀柔区')

# 使用+进行字符串的连接
print(name + school)

# 使用*进行字符串的复制
print((name+'\n')*3)

# 提取name中第一个字符
# 从0开始计数
print(name[0])   # 该句输出的字符为叶
# 中括号取的区间为左闭右开区间，不包括所输入的第二个数字所对应的字符
print(name[0:2])
# 若不指定第二个数字，则会将全部的字符打印出来
print(name[0:])

# 判断"叶"是否包含于变量"name"中，若包含则输出布尔值True
print('叶' in name)
print('叶' not in name)

