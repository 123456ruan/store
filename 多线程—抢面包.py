from threading import Thread
import time

# 全局变量
bread = 500
class Cook(Thread):
    username = ""
    def run(self) -> None:
        global bread
        con = 0
        while True:
            if bread == 500:
                print("篮子已满！！")
                time.sleep(2)
            else:
                bread = bread + 1
                con = con +1
                print(self.username,"造了", con,"面包！！！")

class Person(Thread):
    username = ""
    def run(self) -> None:
        global bread
        money = 300
        con = 0
        while True:
            if money == 0:
                print(self.username,"一共抢了",con,"面包")
                break
            else:
                if bread == 0:
                    print("面包不足，请补充！！")
                    time.sleep(3)
                else:
                    bread = bread - 1
                    money = money - 2.5
                    con = con + 1


c1 = Cook()
c2 = Cook()
c3 = Cook()
p1 = Person()
p2 = Person()
p3 = Person()
p4 = Person()
p5 = Person()
p6 = Person()

c1.username = "张师傅"
c2.username = "李师傅"
c3.username = "王师傅"
p1.username = "1111"
p2.username = "2222"
p3.username = "3333"
p4.username = "4444"
p5.username = "5555"
p6.username = "6666"



c1.start()
c2.start()
c3.start()
p1.start()
p2.start()
p3.start()
p4.start()
p5.start()
p6.start()



