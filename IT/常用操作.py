import math
from turtle import circle, fd

'''
上面这种方式不需要在使用函数时候重申模块名称
但过多引入可能导致和变量名冲突
'''

# # import turtle as t
# circle(200)
# fd(50)

print(1, 2, 3, sep="|", end="abc\n")
print(1, 2, 3, end="abc", sep="|")
# 输出是1|2|3abc

print(4, 5, 6)
# end的默认值是"\n"即换行符，如果不换行，则可以把end替换为空

# 进制转换
x = 100
print(bin(x))
print(oct(x))
print(hex(x))
print(type(bin(x)))  # class 'str'
print(isinstance((bin(x)), str))

# 注意，这些函数会把数据类型转换为str
print(bool(0.1 + 0.2 == 0.3))   # 返回False

# 如果需要判断，可以使用math.isclose()功能
if math.isclose(0.1 + 0.2, 0.3):
    print("1")
else:
    print("0")

# 字符串切片
x = "shanghai china"
x1 = x[0:9]  # [左侧从0开始：右侧不包括：步长]
print(x1)

# try与except
a, b = 1, 0
try:
    # 尝试执行的代码块
    result = a / b
    print("Result is:", result)
except ZeroDivisionError:
    # 如果发生 ZeroDivisionError 异常，则执行这里的代码
    print("Division by zero is not allowed.")

ls = ['x', 'x', x, x, 1, 23, 4, 5]
ls.remove(x)
print(ls)
ls.remove("x")
print(ls)
