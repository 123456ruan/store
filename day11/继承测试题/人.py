'''
i.人：年龄，性别，姓名。
ii.现在有个工种，工人：年龄，性别，姓名 。行为：干活。请用继承的角度来实现该类。
iii.现在有学生这个工种，学生：年龄，性别，姓名，学号。行为：学习，唱歌。请结合上面的几个题目用继承的角度来实现。

'''

class Person:
    __age = 0
    __sex = ""
    __name = ""

    def setAge(self,age):
        self.__age = age
    def getAge(self):
        return self.__age
    def setSex(self,sex):
        self.__sex = sex
    def getSex(self):
        return self.__sex
    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name
# 工人
class Worker(Person):

    def work(self):
        print(self.getName(),"正在干活!")

# 学生
class Student(Person):
    __sid = None
    def setSid(self,sid):
        self.__sid = sid
    def getSid(self):
        return self.__sid