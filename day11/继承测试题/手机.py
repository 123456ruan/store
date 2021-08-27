'''
1、定义老手机类，有品牌属性，且属性私有化，提供相应的getXxx与setXxx方法，提供无返回值的带一个Str类型参数的打电话的方法，内容为：“正在给xxx打电话...”
2、定义新手机类，继承老手机类，重写父类的打电话的方法，内容为2句话：“语音拨号中...”、“正在给xxx打电话...”要求打印“正在给xxx打电话...”这一句调用父类的方法实现，不能在子类的方法中直接打印；提供无返回值的无参数的手机介绍的方法，内容为：“品牌为：xxx的手机很好用...”
3、定义测试类，创建新手机对象，并使用该对象，对父类中的品牌属性赋值；
4、使用新手机对象调用手机介绍的方法；
5、使用新手机对象调用打电话的方法；
'''

import time
class OldPhone:
    __phoneNumber = ""
    __voice = ""
    __brand = ""

    def setPhoneNumber(self,phoneNumber):
        self.__phoneNumber = phoneNumber
    def getPhoneNumber(self):
        return self.__phoneNumber
    def setBrand(self,brand):
        self.__brand = brand
    def getBrand(self):
        return self.__brand
    def setVoice(self,voice):
        self.__voice = voice
    def getVoice(self):
        return self.__voice

    def call(self,number):
        print(self.__phoneNumber,"正在给",number,"打电话","正在响铃：",self.__voice)
        for i in range(8):
            print(".",end="")
            time.sleep(1)

class NewPhone(OldPhone):
    def call(self,number):
        # 1.老功能交给老代码来实现
        print("语音拨号中....")
        super().call(number)
    def show(self):
        print("品牌为：",self.getBrand(),"的手机很好用...")



phone = NewPhone()
phone.setPhoneNumber("12345678978")
phone.setVoice("凤凰传奇")
phone.setBrand("诺基亚")
phone.show()
phone.call("157334256987")





