# �ô�����ʾһ��ð�����򷨣���Ҫʹ��function��ֱ�ӱ�д����
# ����������δ������б�
unsorted_list = [5, 3, 8, 1, 2, 7, 4, 6]

# ð������ʵ��
for i in range(len(unsorted_list)):
    for j in range(len(unsorted_list) - i - 1):  # ÿ��ѭ�����Լ���һ���Ƚϴ���
        if unsorted_list[j] > unsorted_list[j + 1]:  # ���ǰһ��Ԫ�ش��ں�һ��Ԫ�أ��򽻻�λ��
            unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]

# ����������б�
print("Sorted list:", unsorted_list)
