def summ(*args):
    result = 0  # 初始化结果为0
    for num in args:  # 遍历所有输入参数
        result += num  # 累加每个参数到结果中
    return result  # 返回最终结果


print(summ(1, 2, 3, 4, 5))  # 输出15


def greet(name, message):
    print(f"Hello, {name}! {message}")


greet(message="Nice to meet you!", name="John")


def greet(name, message):
    print(f"Hello, {name}! {message}")


greet("John", "Nice to meet you!")
