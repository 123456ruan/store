'''
    猜数字游戏：
        1.系统随机产生一个随机数字（0~1000）
        2.用户从键盘输入数字，与随机数字进行比对 （让用户循环输入20）
            若大了：温馨提示，大了
            若小了：温馨提示，小了
            猜中
        3.循环：一直到猜中为止，退出程序。
    技术分析：
    1.随机数
        random
    2.input
    3.判断
        if ...elif ...else
    4.循环
        while : 当型循环条件型循环
    5.退出程序
        break
    任务：
        加入初始化金币功能，猜错1次扣500金币。
        猜中直接奖励10000，询问是否继续第二轮随机数猜测。

        10次没猜中，系统直接锁定。
'''
# 让系统随机产生一个随机数
import random
num = random.randint(0,100)
#计算输入的次数
count = 0
#当前金币总数
gold = 7000
#提示信息
print("猜数字游戏，每猜错一次金币减500，猜对一次金币加10000，连续猜错10次系统自动退出")
print("*"*80)
while True:
    print("现在金币数为：",gold)
    #判断金币和执行次数
    if gold == 0 or count == 10:
        print("金币不足或连续输入10次错误，系统自动退出")
        break
    else:
        count = count + 1
        chose = input("请输入本次猜的数字：")
        chose = int(chose)
        #判断输入的数字与随机生成的数字
        if chose > num:
            print("大了！")
            gold = gold - 500
        elif chose < num:
            print("小了！")
            gold = gold - 500
        else:
            gold = gold + 10000
            print("恭喜，本次猜中，本次幸运数字为：",num,"，本次猜了",count,"次",",金币总数为：",gold)
            judge = input("是否还要继续,如果继续请输入Y或y,否则输入N或n退出系统:")
            #判断是否要继续
            if judge == "Y" or judge == "y":
                count = 0
                num = random.randint(0, 100)
                continue
            else:
                break















