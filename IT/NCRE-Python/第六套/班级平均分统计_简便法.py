# coding = utf-8

fi = open('data.txt', 'r')
d = {}
students = fi.readlines()
for i in students:
    i = i.strip().split(':')
    clas, score = i[1].split(',')
    # �ֵ�d��key��str��ʽ�İ༶���ƣ�value��һ���б��б���Ԫ���Ǹð༶��ͬѧ���ܷ�
    d[clas] = d.get(clas, []) + [eval(score)]

for i in d:
    # ����i���������ֵ�d��key�����༶���ƣ�sum�����ֵ��value���б����ͣ������ð༶��ͬѧ���ܷ�
    # ע��d[i]��һ���б�����Ҫʹ��len()�������б���
    avg_score = sum(d[i]) / len(d[i])
    # ƽ������Ҫʹ��format()��ʽ��������������뵽С�������λ
    print('{}:{:.2f}'.format(i, avg_score))
