# 创建一个列表
fruits = ['apple', 'banana']

# 使用append()添加元素
fruits.append('cherry')
print(fruits)  # 输出: ['apple', 'banana', 'cherry']

# 使用insert()在指定位置添加元素
fruits.insert(1, 'orange')
print(fruits)  # 输出: ['apple', 'orange', 'banana', 'cherry']

# 使用extend()将另一个列表追加到原列表
fruits.extend(['mango', 'papaya'])
print(fruits)  # 输出: ['apple', 'orange', 'banana', 'cherry', 'mango', 'papaya']
# 注意extend追加列表的功能无法使用append实现

# 使用del删除指定索引的元素
del fruits[1]
print(fruits)  # 输出: ['apple', 'banana', 'cherry', 'mango', 'papaya']

# 使用remove()删除第一次出现的指定元素
fruits.remove('banana')
print(fruits)  # 输出: ['apple', 'cherry', 'mango', 'papaya']

# 使用pop()移除并返回指定索引的元素
fruits.pop(1)
print(fruits)  # 输出: ['apple', 'cherry', 'papaya']

fruits = ['apple', 'cherry', 'papaya']
# 使用clear()移除列表中的所有元素
fruits.clear()
print(fruits)  # 输出: []

fruits = ['apple', 'cherry', 'papaya']
# 使用sort()对列表进行排序
fruits.sort()
print(fruits)  # 输出: ['apple', 'cherry', 'papaya']

# 使用reverse()反转列表
fruits.reverse()
print(fruits)  # 输出: ['papaya', 'cherry', 'apple']

# 使用index()查找元素索引
print(fruits.index('cherry'))  # 输出: 1

# 使用count()计算元素出现次数
print(fruits.count('cherry'))  # 输出: 1

# 使用copy()创建列表的浅拷贝
fruits_copy = fruits.copy()
print(fruits_copy)  # 输出: ['cherry']

# 使用len()获取列表长度
print(len(fruits))  # 输出: 1

num = [1, 2, 3, 7, 10]
# 使用max()和min()获取列表中的最大值和最小值
print(max(num))  # 输出: 'cherry'
print(min(num))  # 输出: 'cherry'

# 对列表使用key键进行排序
my_list = [('apple', 3), ('banana', 2), ('cherry', 1), ('date', 4)]
my_list.sort(key=lambda x: x[1])
print(my_list)  # 输出: [('date', 4), ('apple', 3), ('banana', 2), ('cherry', 1)]
