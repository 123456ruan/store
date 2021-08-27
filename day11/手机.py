'''
    EMUI:5.0
    6.0
    7.0
    EMUI：11.0
    EMUI: 12.0
    老手机：
        打电话：手机号，归属地，彩铃
    新手机：
        打电话：手机号，归属地，彩铃，大头贴
'''

import time
class OldPhone:
    __phoneNumber = ""
    __address = ""
    __voice = ""

    def setPhoneNumber(self,phoneNumber):
        self.__phoneNumber = phoneNumber
    def getPhoneNumber(self):
        return self.__phoneNumber
    def setAddress(self,address):
        self.__address = address
    def getAddress(self):
        return self.__addressr
    def setVoice(self,voice):
        self.__voice = voice
    def getVoice(self):
        return self.__voice

    def call(self,number):
        print(self.__phoneNumber,"正在给",number,"打电话，归属地为：",self.__address,"正在响铃：",self.__voice)
        for i in range(8):
            print(".",end="")
            time.sleep(1)

class NewPhone(OldPhone):
    picture = ""
    def setpicture(self,voice):
        self.__voice = voice
    def getVoice(self):
        return self.__voice

    def call(self,number):
        # 1.老功能交给老代码来实现
        super().call(number)
        # 2.大头贴显示新手机自己做
        print("个人备注头像显示为：",self.picture)


phone = NewPhone()
phone.phoneNumber = "13552648187"
phone.voice = "月亮之上"
phone.address = "北京市昌平区"
phone.picture = "野猪佩奇"

phone.call("13678745045")








# phone = OldPhone()
# phone.phoneNumber = "13552648187"
# phone.address = "北京市昌平区"
# phone.voice = "凤凰传奇"
#
# phone.call("15678457484")







