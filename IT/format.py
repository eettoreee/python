# example_1
name = 'zhangsan'
age = 20
sex = 'man'
# 注意format函数的用法
print('i am {0} ,i am {1} years old,and i am a {2}'.format(name, age, sex))

# example_2
a = 1
b = 2
c = 3
amount = a + b + c
# 此处的加号后面需要将amount变量的格式改为字符串（str），字符串和浮点两种数据类型无法同时print
print('所求的和为：' + str(amount))
