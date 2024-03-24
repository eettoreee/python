import random

word_list = ["apple", "banana", "orange"]
answer = random.choice(word_list)
print(answer)

blanks = []
for i in range(1, len(answer) + 1):
    blanks += "_"

# print(len(answer))
# 使用enumerate同时输出数据和索引


hp = 5
while not "".join(blanks) == answer:
    guess = input("输入你的猜测：").lower()

    # 替换下划线方法1
    # for position in range(0, len(answer)):  # 替换下划线，有几个换几个
    #     word = answer[position]
    #     if guess == word:  # 判断单词是否匹配
    #         blanks[position] = word

    # 替换下划线方法2
    for value, letter in enumerate(answer):  # 注意enumerate()用法
        if letter == guess:
            blanks[value] = letter

    print(blanks)
    if guess not in answer:  # 如果不匹配的话要在for循环外，while循环内来执行减命
        hp -= 1
    # print(hp)
    if hp == 0:  # 判断血量状态
        print("you lost")
        break
else:
    print("you_win")
