def check_int(num):
    a = float(num)
    if abs(int(a)) - abs(a) == 0:
        print('Yes')
    else:
        print('No')


print('this function can help you with checking number')
check_int(input('input the num that u r going to check:'))
