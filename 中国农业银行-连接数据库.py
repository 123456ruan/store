import random
from DBUtils import update
from DBUtils import select
from DBUtils import select2

# 银行名称
bank_name = "中国农业银行昌平区回龙观分行"
def welcome():
    print("-"*20+"欢迎使 用中国农业银行"+"-"*25)
    print("- 1.开户")
    print("- 2.存钱")
    print("- 3.取钱")
    print("- 4.转账")
    print("- 5.查询")
    print("- 6.Bye")
    print("-" * 60)
# 银行开户逻辑
def bank_addUser(account, type, name, password, country, province, street, House_number):
    sql = "SELECT COUNT(*) FROM ny_bank"
    data= select(sql,[])
    sql1 = "select * from ny_bank where account = %s"
    n = select2(sql1, account)
    if data[0][0] >= 100:
        return 3
    elif n != 0:
        return 2
    # 正常开户
    else:
        sql2 = "insert into ny_bank values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        param = [account, type, name, password, country, province, street, House_number, 0, bank_name]
        update(sql2, param)
        return 1
# 添加开户方法
def addUser():
    account = random.randint(10000000, 99999999)
    print("账户:", account)
    type = input("请输入类型：")
    name = input("请输入用户名：")
    password = input("请输入密码：")
    country = input("请输入国家：")
    province = input("请输入省份：")
    street = input("请输入街道：")
    House_number = input("请输入门牌号：")
    n = bank_addUser(account,type,name,password,country,province,street,House_number)
    if n == 1:
        print("恭喜开户成功！！！")
        print("-"*20+"账户信息"+"-"*20)
        str = "账户：%s\n"+"类型：%s\n"+"用户名：%s\n"+"密码：%s\n"+"国家：%s\n\t"+\
              "省份：%s\n\t"+"街道：%s\n\t"+"门牌号：%s\n"+"账户余额：%s\n"+"开户行：%s"
        print(str % (account, type, name, password, country, province, street,
                     House_number, 0, bank_name))
        print("-" * 55)
    elif n == 2:
        print("该用户已经存在！！！")
    else:
        print("该银行账户已满，不能开户")
# 存钱方法
def saveMoney():
    account = input("请输入账户：")
    if select2("select * from ny_bank where account = %s",account) != 0:
        money = int(input("请输入存款金额："))
        sql = "update ny_bank set money = money + %s where account = %s"
        param=[money,account]
        update(sql,param)
        print("存款成功！！！！")
    else:
        print("该账户不存在!!!!")
# 取钱方法
def withdrawMoney():
    account = input("请输入账户：")
    password = input("请输入账户密码：")
    param =[account,password]
    if select2("select * from ny_bank where account = %s and password = %s ",param) != 0:
        money = int(input("请输入取款金额："))
        sql = "update ny_bank set money = money - %s where account = %s"
        param1 = [money,account]
        update(sql,param1)
        print("取款成功！！！！！")
    else:
        print("该账户不存在或密码错误！！！！")
# 转账
def transfer():
    account1 = input("请输入转出账户：")
    account2 = input("请输入转入账户：")
    if select2("select * from ny_bank where account = %s  ",account1):
        if select2("select * from ny_bank where account = %s  ", account2):
            password = input("请输入转出账户密码：")
            param = [account1,password]
            if select2("select * from ny_bank where account = %s and password = %s",param):
                money = int(input("请输入转出金额："))
                money1 = select("select money from ny_bank where account = %s",account1)
                print(money1)
                print(money1[0][0])
                if money < money1[0][0]:
                    type = select("select type from ny_bank where account = %s", account1)
                    param1 = [money,account1]
                    param2 = [money,account2]
                    print(type)
                    if type[0][0] == "1" and money < 50000:
                        update("update ny_bank set money = money - %s where account = %s",param1)
                        update("update ny_bank set money = money + %s where account = %s", param2)
                        print("转入成功！！！！")
                    elif type[0][0]  == "2" and money < 20000:
                        update("update ny_bank set money = money - %s where account = %s", param1)
                        update("update ny_bank set money = money - %s where account = %s", param2)
                        print("转入成功！！！！")
                    else:
                        print("1.类账户:转出最大5万,2.类账户：转出最大2万")
                else:
                    print("余额不足，不能转出！！！！")
            else:
                print("账户密码不正确，请重新办理业务！！！！")
        else:
            print("转入的账户不正确，请重新办理业务！！！")
    else:
        print("转出的账户不正确，请重新办理业务！！！")
# 查询
def getSelect():
    account = input("请输入账户：")
    if select2("select * from ny_bank where account = %s",account) != 0:
        password = input("请输入账户密码：")
        if select2("select * from ny_bank where password = %s",password) != 0:
            data = select("select * from ny_bank where account = %s",account)
            print("-" * 25 + "账户信息" + "-" * 25)
            str = "账户：%s\n" + "类型：%s\n" + "用户名：%s\n" + "密码：%s\n" + "国家：%s\n\t" + \
                  "省份：%s\n\t" + "街道：%s\n\t" + "门牌号：%s\n" + "账户余额：%s\n" + "开户行：%s"
            print(str % (data[0][0],data[0][1],data[0][2],data[0][3],data[0][4],data[0][5],
                         data[0][6],data[0][7],data[0][8],data[0][9]))
            print("-" * 60)
        else:
            print("密码错误!!!!")
    else:
        print("该账户不存在!!!!")
# 实现
while True:
    welcome()
    num = input("请输入您的业务编号：")
    if num.isdigit():
        num = int(num)
        if num == 1:
            addUser()
        elif num == 2:
            saveMoney()
        elif num == 3:
            withdrawMoney()
        elif num == 4:
            transfer()
        elif num == 5:
            getSelect()
        elif num == 6:
            print("欢迎下次使用！！！")
            break
        else:
            print("输入非法字符！！！,请选择正确的业务")
    else:
        print("您输入的字符为非法！！，请输入正确的字符!!!!")


