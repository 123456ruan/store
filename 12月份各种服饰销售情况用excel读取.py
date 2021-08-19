import xlrd

# 打开
wb = xlrd.open_workbook(filename = r"D:\python自动化测试1\python\day07\12月份衣服销售数据.xlsx")

# 选择选项卡
data = {}
st = wb.sheet_by_name("12月份各种服饰销售情况")
for j in range(1, st.nrows):
    if st.cell(j, 1).value in data:
        data[st.cell(j, 1).value]["数量"] = data[st.cell(j, 1).value]["数量"] + st.cell(j, 4).value
    else:
        data[st.cell(j, 1).value] = {"数量": st.cell(j, 4).value, "单价": st.cell(j, 2).value}
print(data)
# 全年的销售总额
sum = 0
for key in data:
    sum = data[key]["数量"]*data[key]["单价"] + sum
print("12月的销售总额",sum)
# 每件衣服的销售额占比
for i in data:
    print("%s的销售额的占比：" % i,round(data[i]["数量"]*data[i]["单价"]/sum*100,2),"%")
# 销售总数量
num = 0
for i in data:
    num = data[key]["数量"] + num
# 每件衣服的销售（件数）占比
for i in data:
    print("%s的销售（件数）占比：" % i,round(data[i]["数量"]/num*100,2),"%")