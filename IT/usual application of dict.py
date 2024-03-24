# 创建一个字典
my_dict = {'name': 'Tom', 'age': 20, 'city': 'New York'}

# 访问字典的值
print(my_dict['name'])  # 输出: Tom

# 修改字典的值
my_dict['age'] = 21
print(my_dict['age'])  # 输出: 21

# 删除字典的值
del my_dict['city']
print(my_dict)  # 输出: {'name': 'Tom', 'age': 21}

# 获取字典的所有键
keys = my_dict.keys()
print(keys)  # 输出: dict_keys(['name', 'age'])

# 获取字典的所有值
values = my_dict.values()
print(values)  # 输出: dict_values(['Tom', 21])

# 获取字典的所有键值对
items = my_dict.items()
print(items)  # 输出: dict_items([('name', 'Tom'), ('age', 21)])

# for遍历字典的用法（嵌套）
nested_dict = {'key1': {'subkey1': 'value1', 'subkey2': 'value2'},
               'key2': {'subkey3': 'value3'}}


# 字典的pop用法演示例
def pop_nested_dict(d):
    """
    从嵌套字典中删除键值对

    参数:
    d - 一个嵌套的字典对象，其中的值可以是任意类型的字典。

    返回值:
    无返回值，该函数仅删除字典中指定的键值对。
    """
    for key, value in d.items():
        # 如果当前值是一部字典，则递归遍历这个字典
        if isinstance(value, dict):
            pop_nested_dict(value)
        else:
            # 如果当前值不是字典，则删除键值对
            d.pop(key)


def traverse_nested_dict(d):
    """
    遍历嵌套字典

    参数:
    d - 一个嵌套的字典对象，其中的值可以是任意类型的字典。

    返回值:
    无返回值，该函数仅打印字典中每个键值对。
    """
    for key, value in d.items():
        # 如果当前值是一部字典，则递归遍历这个字典
        if isinstance(value, dict):
            traverse_nested_dict(value)
        else:
            # 如果当前值不是字典，则打印键和值
            print(f"Key: {key}, Value: {value}")


traverse_nested_dict(nested_dict)
