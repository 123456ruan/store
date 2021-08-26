'''
分析一个水杯的属性和功能，使用类描述并创建对象
高度，容积，颜色，材质
能存放液体
'''
class Water_cup:
    # 高度
    height = 0
    # 容积
    valume = 0
    # 颜色
    color = ""
    # 材质
    texture_of_material = ""

    def deposit(self):
        print(self.texture_of_material,"和",self.color,"的水杯","能存放液体")
wp = Water_cup()
wp.color = "黄色"
wp.texture_of_material = "塑料材质"
wp.height = 100
wp.valume = 500
wp.deposit()

'''
有笔记本电脑
（屏幕大小，价格，cpu型号，内存大小，待机时长），
行为（打字，打游戏，看视频）
'''
class Computer:
    height = 0
    weight = 0
    price = 0
    cpu = ""
    memory = ""
    time = 0

    def typing(self):
        print("可以打字！！！！！！")
    def game(self):
        print("可以打游戏！！！！！！")
    def watch_TV(self):
        print("可以看电视！！！！")
    def show(self):
        print(self.height,"X",self.weight,"的电视","价格：",self.price,"cpu型号：",self.cpu,"内存大小：",self.memory,"待机时长",self.time)
co = Computer()
co.height = 50
co.weight = 100
co.price = 20000
co.cpu = "I7"
co.memory = "8"
co.time = 24
co.typing()
co.watch_TV()
co.game()
co.show()