# 用代码演示一下冒牌排序法，不要使用function，直接编写即可
# 假设有如下未排序的列表
unsorted_list = [5, 3, 8, 1, 2, 7, 4, 6]

# 冒泡排序实现
for i in range(len(unsorted_list)):
    for j in range(len(unsorted_list) - i - 1):  # 每轮循环可以减少一个比较次数
        if unsorted_list[j] > unsorted_list[j + 1]:  # 如果前一个元素大于后一个元素，则交换位置
            unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]

# 输出排序后的列表
print("Sorted list:", unsorted_list)
