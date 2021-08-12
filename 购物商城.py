'''
    商城：
        1.初始化钱包余额
        2.推个空的购物车
        3.正常购物：
            输入商品的编号
            看是否有这个商品
                有：
                    看钱是否足够
                        够：
                            添加到购物车里
                            余额减去相对应的钱
                        不够：
                            温馨：穷鬼，别瞎弄！请买个其他商品
                没有：
                    买个其他商品，别瞎弄！
        4.打印购物小条
    任务：
        1.购物小条的商品重复打印问题
        2.  10张联想电脑 0.5，  20老干妈优惠券 0.1 ， 15 华为优惠券 0.6
            随机抽取一张优惠券，在结算的时候进行打折，进行结算。
'''
import random
def youhui(n):
    if n>=1 and n<=10:
        print("恭喜你获得了一张联想的优惠卷")
        return 1
    elif n>=11 and n<=35:
        print("恭喜你获得一张老干妈的优惠卷")
        return 2
    else:
        print("恭喜你获得一张华为的优惠卷")
        return 3

shop = [
    ["lenovo PC",5000],
    ["Mac pc",12000],
    ["HUAWEI  WATCH PRO 20",2000],
    ["机械革命",15000],
    ["老干妈",7.5],
    ["卫龙辣条",3],
    ["西瓜",2]
]
# 1.空的购物车
mycart = []
#  2.初始化您的余额
money = input("请输入您本月工资：")
money = int(money)
# 3.正常购物
i = 1
n = youhui(random.randint(0, 45))
while i <= 20:
    # 展示商品
    for key, value in enumerate(shop):
        print(key, value)
    chose = input("请输入您想要的商品：")
    if chose.isdigit():
        chose = int(chose)
        if chose > len(shop): # len
            print("没有改号商品！请重新输入！")
        else:
            # 钱够不够
            if money >= shop[chose][1]:
                mycart.append(shop[chose])
                j = 0
                if n == 0:
                    money = money - shop[chose][1]
                else:
                    if chose == 0 and n == 1 :
                        y = input("是否使用优惠卷：")
                        if  y == "Y" or y == "y":
                            money = money - 0.5 * shop[chose][1]
                            n = 0;
                        else:
                            money = money - shop[chose][1]
                    elif chose == 4 and n == 2 :
                        y = input("是否使用优惠卷：")
                        if y == "Y" or y == "y":
                            money = money - 0.1 * shop[chose][1]
                            n = 0;
                        else:
                            money = money - shop[chose][1]
                    elif chose == 2 and n == 3:
                        y = input("是否使用优惠卷：")
                        if y == "Y" or y == "y":
                            money = money - 0.6 * shop[chose][1]
                            n = 0;
                        else:
                            money = money - shop[chose][1]
                    else:
                        money = money - shop[chose][1]
                print("恭喜，添加成功！您的余额还剩",money)
            else:
                print("穷鬼，钱不够了，别瞎弄！买其他商品吧！")
    elif chose == "q" or chose == "Q":
        print("欢迎下次光临！")
        break  # 跳出循环
    else:
        print("对不起，您输入错误，别瞎弄！")
    i = i + 1

print("以下是您的购物小条，请拿好！")
num= []
print("---------------------------------------")
#统计商品出现的次数
for key,value  in enumerate(mycart):
    if value in mycart[:key]:
        continue
    else:
         num.append(mycart.count(mycart[key]))
mycart = list(set([tuple(t) for t in mycart]))
for k in mycart:
    mycart[mycart.index(k)] = list(k)
for key,value  in enumerate(mycart):
    print(key,"------",value[0],"价格：￥",value[1],"数量：",num[key])
print("---------------------------------------")
print("您的余额还剩：￥",money)


































