import random
# 用户
users = {
    11111111:{
        "type":"1",
        "name":"111",
        "password":"123456",
        "country":"111",
        "province":"111",
        "street":"111",
        "House_number":"111",
        "money":10000,
        "bank_name":"中国农业银行"
    }
}
# 银行名称
bank_name = "中国农业银行"
def welcome():
    print("-"*20+"欢迎使用中国农业银行"+"-"*20)
    print("1.开户")
    print("2.存钱")
    print("3.取钱")
    print("4.转账")
    print("5.查询")
    print("6.Bye")
    print("-" * 60)
# 银行开户逻辑
def bank_addUser(account, type, name, password, country, province, street, House_number):
    if len(users) > 100:
        return 3
    else:
        if account in users:
            return 2
        else:
            # 正常开户
            users[account] = {
                "type": type,
                "name": name,
                "password": password,
                "country": country,
                "province": province,
                "street": street,
                "House_number": House_number,
                "money": 0,
                "bank_name": bank_name
            }
            return 1
# 添加开户方法
def addUser():
    account = random.randint(10000000, 99999999)
    print("账户为:", account)
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
        str = "账户：%s\n"+"类型：%s\n"+"用户名：%s\n"+"密码：%s\n"+"国家：%s\n"+\
              "省份：%s\n"+"街道：%s\n"+"门牌号：%s\n"+"账户余额：%s\n"+"开户行：%s"
        print(str % (account, type, name, password, country, province, street,
                     House_number, users[account]["money"], bank_name))
        print("-" * 55)
    elif n == 2:
        print("该用户已经存在！！！")
    else:
        print("该银行账户已满，不能开户")
# 存钱方法
def saveMoney():
    account = int(input("请输入账户："))
    if account in users:
        money = int(input("请输入存款金额："))
        users[account]["money"] = money + int(users[account]["money"])
        print("存款成功！！！！")
    else:
        print("该账户不存在!!!!")
# 取钱方法
def withdrawMoney():
    account = int(input("请输入账户："))
    if account in users:
        password = input("请输入账户密码：")
        if password == users[account]["password"]:
            money = int(input("请输入取款金额："))
            users[account]["money"] =int(users[account]["money"])-money
            print("取款成功！！！！！")
        else:
            print("用户密码不正确！！！！")
    else:
        print("该账户不存在！！！！")
# 转账
def transfer(account1, account2):
    password = input("请输入转出账户密码：")
    if password == users[account1]["password"]:
        money = int(input("请输入转出金额："))
        n = cost(money)
        if money < int(users[account1]["money"]):
            if users[account1]["type"] == "1" and money < 50000:
                users[account1]["money"] = float(users[account1]["money"]) - money - n
                users[account2]["money"] = int(users[account2]["money"]) + money
                print("转出账户余额：",users[account1]["money"])
                print("转入账户余额：",users[account2]["money"])
                print("转入成功！！！！")
            elif users[account1]["type"] == "2" and money < 20000:
                users[account1]["money"] = float(users[account1]["money"]) - money - n
                users[account2]["money"] = int(users[account2]["money"]) + money
                print("转账成功！！！！")
            else:
                print("1.类账户:转出最大5万,2.类账户：转出最大2万")

        else:
            print("余额不足，不能转出！！！！")
    else:
        print("账户密码不正确，请重新办理业务！！！！")
# 汇率
def cost(money):
    if money <= 2000:
        return 1.6
    elif money > 2000 and money <= 5000:
        return 4
    elif money > 5000 and money <=10000:
        return 8
    elif money > 10000 and money <= 50000:
        return 12
    else:
        return money*0.3
# 跨行转账
def transfer2():

    account1 = int(input("请输入转出账户："))
    account2 = int(input("请输入转入账户："))
    from test_GSbank import users1
    # 本行转账
    if account1 in users and account2 in users:
        transfer(account1,account2)
    elif account2 in users1 and account1 in users:
        # 跨行转账
        password = input("请输入转出账户密码：")
        if password == users[account1]["password"]:
            money = int(input("请输入转出金额："))
            n = cost(money)
            if money < int(users[account1]["money"]):
                if users[account1]["type"] == "1" and money < 50000:
                    users[account1]["money"] = float(users[account1]["money"]) - money - n
                    users1[account2]["money"] = int(users1[account2]["money"]) + money
                    print("转入成功！！！！")
                    print("转入账户金额：",users1[account2]["money"])
                    print("转出账户金额：",users[account1]["money"])
                elif users[account1]["type"] == "2" and money < 20000:
                    users[account1]["money"] = float(users[account1]["money"]) - money - n
                    users1[account2]["money"] = int(users1[account2]["money"]) + money
                    print("转入成功！！！！")
                    print("转入账户金额：", users1[account2]["money"])
                    print("转出账户金额：", users[account1]["money"])
                else:
                    print("1.类账户:转出最大5万,2.类账户：转出最大2万")
        else:
            print("密码不正确！！")
    else:
        print("账户不正确！！！")
# 查询
def getSelect():
    account = int(input("请输入账户："))
    from test_GSbank import users1
    if account in users:
        password = input("请输入账户密码：")
        if password == users[account]["password"]:
            print("-" * 20 + "账户信息" + "-" * 20)
            str = "账户：%s\n" + "类型：%s\n" + "用户名：%s\n" + "密码：%s\n" + "国家：%s\n" \
                  + "省份：%s\n" + "街道：%s\n" + "门牌号：%s\n" + "账户余额：%s\n" + "开户行：%s"
            print(str % (account,  users[account]["type"],
                         users[account]["name"], users[account]["password"],
                         users[account]["country"], users[account]["province"],
                         users[account]["street"], users[account]["House_number"],
                         users[account]["money"], bank_name))
            print("-" * 55)
        else:
            print("密码错误!!!!")
    elif account in users1:
        password = input("请输入账户密码：")
        if password == users1[account]["password"]:
            print("-" * 20 + "账户信息" + "-" * 20)
            str = "账户：%s\n"  + "用户名：%s\n" + "密码：%s\n" + "国家：%s\n" \
                  + "省份：%s\n" + "街道：%s\n" + "门牌号：%s\n" + "账户余额：%s\n" + "开户行：%s"
            print(str % (account,users1[account]["name"], users1[account]["password"],
                         users1[account]["country"], users1[account]["province"],
                         users1[account]["street"], users1[account]["House_number"],
                         users1[account]["money"], users1[account]["bank_name"]))
            print("-" * 55)

    else:
        print("该账户不存在!!!!")
# 实现
def index():
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
                transfer2()
            elif num == 5:
                getSelect()
            elif num == 6:
                print("欢迎下次使用！！！")
                break
            else:
                print("输入非法字符！！！,请选择正确的业务")
        else:
            print("您输入的字符为非法！！，请输入正确的字符!!!!")
if __name__ == "__main__":
    index()


