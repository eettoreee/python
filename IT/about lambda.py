# ����һ����׼��def�������������������ĺ�
def add_normal(x, y):
    return x + y


# ʹ��lambda������ͬ���ܵ���������
add_lambda = lambda x, y: x + y  # lambda�����Ķ��巽ʽ��lambda �����б�: ���ʽ

# ���Ա�׼������lambda������Ч������ͬ��
print(add_normal(3, 5))  # �����8
print(add_lambda(3, 5))  # �����8

# ʾ��2������lambda������Ϊkey������������
numbers = [(4, 'apple'), (1, 'banana'), (3, 'cherry')]
# ʹ��lambda��������Ԫ���еĵ�һ��Ԫ�أ����֣�������������
numbers.sort(key=lambda x: x[0])  # reverseĬ��ΪFalse������������
print(numbers)  # �����[(1, 'banana'), (3, 'cherry'), (4, 'apple')]

# ʾ��3����filter������ʹ��lambda���ʽɸѡ��ż��
numbers_list = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers_list)
print(list(even_numbers))  # �����[2, 4, 6]

# ע������ʾ��չʾ��lambda������μ򻯴��벢Ӧ���ڸ߽׺�����sort()��filter()
