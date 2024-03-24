# 定义一个标准的def函数，用于求两个数的和
def add_normal(x, y):
    return x + y


# 使用lambda定义相同功能的匿名函数
add_lambda = lambda x, y: x + y  # lambda函数的定义方式：lambda 参数列表: 表达式

# 测试标准函数和lambda函数的效果是相同的
print(add_normal(3, 5))  # 输出：8
print(add_lambda(3, 5))  # 输出：8

# 示例2：利用lambda函数作为key参数进行排序
numbers = [(4, 'apple'), (1, 'banana'), (3, 'cherry')]
# 使用lambda函数按照元组中的第一个元素（数字）进行升序排序
numbers.sort(key=lambda x: x[0])  # reverse默认为False，即升序排序
print(numbers)  # 输出：[(1, 'banana'), (3, 'cherry'), (4, 'apple')]

# 示例3：在filter函数中使用lambda表达式筛选出偶数
numbers_list = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers_list)
print(list(even_numbers))  # 输出：[2, 4, 6]

# 注：以上示例展示了lambda函数如何简化代码并应用于高阶函数如sort()和filter()
