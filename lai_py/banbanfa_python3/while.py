# def while_f(nameble2):
#     list1 = []
#     a1 = 0
#     while a1 < nameble2 :
#         a1 = a1+1
#         list1.append(a1)
#     return list1
#
# b = while_f(5)
# print(b)
import random
times = 3
secret = random.randint(1,10)
guess = 0
while(guess != secret)and(times > 0):
    try:
        times = times - 1
        temp = int(input('请输入一个数\n'))
        guess = temp
        print(secret)
        if guess == secret:
            print('猜对了')
        else:
            if guess > secret:
                print('大了')
            else:
                print('小了')
            if times > 0:
                print('再试一次')
            else:
                print('没次数了')
    except:
        print('输入的不是数字')
print('游戏结束')

play_round = 1  # 计算游戏回合
count_list = []  # 每回合猜次数
sign = True
# 计算平均值
def avg(clist):
    sum_count = 0
    for i in clist:
        sum_count += i
    avg_count = sum_count / len(clist)
    return avg_count
player = input('游戏开始，请输入玩家名：\n')
while sign is True:
    correct_num = random.randint(0, 100)
    print('==========第%d回合开始==========' % play_round)
    print('正确答案：%d' % correct_num)
    temp_count = 0  # temp每回合猜的次数
    while True:
        temp_count += 1
        try:
            guess_num = int(input('猜数字:\n'))
            if guess_num == correct_num:
                print('你猜对惹！本回合共猜了%d次' % temp_count)
                break
            elif guess_num > correct_num:
                print('不对，请往小了猜。')

            elif guess_num < correct_num:
                print('不对，请往大了猜。')

        except ValueError as verr:
            print('请输入数字,游戏重新开始！')
            break
    count_list.append(temp_count)
    print('==========第%d回合结束==========' % play_round)
    play = input('再来一回合吗[yes]\n')
    #     print(count_list)
    if play == 'yes':
        play_round += 1
        sign = True
    else:
        min_count = min(count_list)
        sum_count = avg(count_list)

        with open('%splayrecord.txt' % player, 'a+', encoding='utf-8') as f:
            f.write('玩家：' + player + '\n')
            f.write('总共玩了%d回合，最快%d次猜出正确答案，平均%d猜出\n' % (play_round, min_count, sum_count))
        print('游戏结束！')
        print('总共玩了%d回合，最快%d次猜出正确答案，平均%d猜出\n' % (play_round, min_count, sum_count))
        sign = False