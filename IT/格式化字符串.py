# 格式化字符串
# %s表示任意字符 %d表示整数 %f表示浮点数
name = 'jack'
age = 20
sex = 'man'

# 表达单个变量时
# message = 'i am %s' % name

# 当需要表达多个变量时
# message = 'i am %s, i am %s years old,i am a %s' % (name, age, sex)
# print(message)

# 当在%和s之间添加数字时，表示字符串最小的长度为该数字，不足时候将在字符前用空格代替
# message = 'i am %1s' % name
# print(message)

# 当在%和s之间添加小数时,表示最少数字.个，最多.数字个
# message = 'i am %1.2s' % name
# print(message)


# 使用format函数进行格式化字符串 略


# 在变量前添加f可以直接使用格式化字符串
message = f'i am {name},i am {age} years old,i am a {sex}.'
print(message)


# 总结
# 1,能够更好的在不同平台(桌面,WEB),都能实现统一的数据展示
# 2,在当前的应用软件系统中使用格式化进行日志的输出,方便对系统输出的数据进行分析,进而优化程序
# 3,python中不能使用"+"对不同类型的数据实现数据拼接

