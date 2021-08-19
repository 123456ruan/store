import xlrd

wd = xlrd.open_workbook(filename=r"D:\python自动化测试1\python\day07\2020年每个月的销售情况.xlsx")
i = 0
data={}
for i in range(12):
    st = wd.sheet_by_index(i)
    for j in range(1,st.nrows):
         if st.cell(j,1).value in data:
             data[st.cell(j,1).value]["数量"] = data[st.cell(j,1).value]["数量"] + st.cell(j,4).value
         else:
             data[st.cell(j,1).value] = {"数量":st.cell(j,4).value,"单价":st.cell(j,2).value}
print(data)
# 全年的销售总额
sum = 0
for key in data:
    sum = data[key]["数量"]*data[key]["单价"] + sum
print("全年的销售总额",sum)
# 销售总数量
num = 0
for i in data:
    num = data[key]["数量"] + num
# 每件衣服的销售（件数）占比
for i in data:
    print("%s的销售（件数）占比：" % i,data[i]["数量"]/num)
# 每件衣服的月销售占比
#第一个月
one={}
num1 = 0
st = wd.sheet_by_index(0)
for j in range(1,st.nrows):
     if st.cell(j,1).value in one:
         one[st.cell(j,1).value]["数量"] = one[st.cell(j,1).value]["数量"] + st.cell(j,4).value
         num1 = num1 + st.cell(j,4).value
     else:
         one[st.cell(j,1).value] = {"数量":st.cell(j,4).value,"单价":st.cell(j,2).value}
         num1 = num1 + st.cell(j, 4).value
print("第一个月",one)
for i in one:
    print("第一个月%s的销售的占比：" % i,one[i]["数量"]/num1)
#第二个月
two={}
num2 = 0
st = wd.sheet_by_index(1)
for j in range(1,st.nrows):
     if st.cell(j,1).value in two:
         two[st.cell(j,1).value]["数量"] = two[st.cell(j,1).value]["数量"] + st.cell(j,4).value
         num2 = num2 + st.cell(j,4).value
     else:
         two[st.cell(j,1).value] = {"数量":st.cell(j,4).value,"单价":st.cell(j,2).value}
         num2 = num2 + st.cell(j, 4).value
print("第二个月",two)
for i in two:
    print("第二个月%s的销售的占比：" % i,two[i]["数量"]/num2)
# 第三个月
three={}
num3 = 0
st = wd.sheet_by_index(2)
for j in range(1,st.nrows):
     if st.cell(j,1).value in three:
         three[st.cell(j,1).value]["数量"] = three[st.cell(j,1).value]["数量"] + st.cell(j,4).value
         num3 = num3 + st.cell(j,4).value
     else:
         three[st.cell(j,1).value] = {"数量":st.cell(j,4).value,"单价":st.cell(j,2).value}
         num3 = num3 + st.cell(j, 4).value
print("第三个月",three)
for i in three:
    print("第三个月%s的销售的占比：" % i,three[i]["数量"]/num3)
# 第四个月
four={}
num4 = 0
st = wd.sheet_by_index(3)
for j in range(1,st.nrows):
     if st.cell(j,1).value in four:
         four[st.cell(j,1).value]["数量"] = four[st.cell(j,1).value]["数量"] + st.cell(j,4).value
         num4 = num4 + st.cell(j,4).value
     else:
         four[st.cell(j,1).value] = {"数量":st.cell(j,4).value,"单价":st.cell(j,2).value}
         num4 = num4 + st.cell(j, 4).value
print("第四个月",four)
for i in four:
    print("第四个月%s的销售的占比：" % i,four[i]["数量"]/num4)
print("其他月份类同。。。。。。。。")
# 每件衣服的销售额占比
for i in data:
    print("%s的销售额的占比：" % i,data[i]["数量"]*data[i]["单价"]/sum)
# 最畅销的衣服是那种
# 求最大的销售量
def max(data):
    n = 0
    for i in data:
        if n < data[i]["数量"]:
            n = data[i]["数量"]
            name1 = i
        else:
            continue
    return name1

print("最畅销的衣服是：", max(data))
# 每个季度最畅销的衣服
#第一季度
data1={}
for i in range(1,4):
    st = wd.sheet_by_index(i)
    for j in range(1,st.nrows):
         if st.cell(j,1).value in data1:
             data1[st.cell(j,1).value]["数量"] = data1[st.cell(j,1).value]["数量"] + st.cell(j,4).value
         else:
             data1[st.cell(j,1).value] = {"数量":st.cell(j,4).value,"单价":st.cell(j,2).value}
print("第一季度：",data1)
print("第一季度最畅销的衣服是：", max(data1))
#第二季度
data2={}
for i in range(4,7):
    st = wd.sheet_by_index(i)
    for j in range(1,st.nrows):
         if st.cell(j,1).value in data2:
             data2[st.cell(j,1).value]["数量"] = data2[st.cell(j,1).value]["数量"] + st.cell(j,4).value
         else:
             data2[st.cell(j,1).value] = {"数量":st.cell(j,4).value,"单价":st.cell(j,2).value}
print("第二季度：",data2)
print("第二季度最畅销的衣服是：", max(data2))
#第三季度
data3={}
for i in range(7,10):
    st = wd.sheet_by_index(i)
    for j in range(1,st.nrows):
         if st.cell(j,1).value in data3:
             data3[st.cell(j,1).value]["数量"] = data3[st.cell(j,1).value]["数量"] + st.cell(j,4).value
         else:
             data3[st.cell(j,1).value] = {"数量":st.cell(j,4).value,"单价":st.cell(j,2).value}
print("第三季度：",data3)
print("第三季度最畅销的衣服是：", max(data3))
# 第四季度
data4={}
for i in range(10,11):
    st = wd.sheet_by_index(i)
    for j in range(1,st.nrows):
         if st.cell(j,1).value in data4:
             data4[st.cell(j,1).value]["数量"] = data4[st.cell(j,1).value]["数量"] + st.cell(j,4).value
         else:
             data4[st.cell(j,1).value] = {"数量":st.cell(j,4).value,"单价":st.cell(j,2).value}
for i in range(0,1):
    st = wd.sheet_by_index(i)
    for j in range(1,st.nrows):
         if st.cell(j,1).value in data4:
             data4[st.cell(j,1).value]["数量"] = data4[st.cell(j,1).value]["数量"] + st.cell(j,4).value
         else:
             data4[st.cell(j,1).value] = {"数量":st.cell(j,4).value,"单价":st.cell(j,2).value}
print("第四季度：",data4)
print("第四季度最畅销的衣服是：", max(data4))
# 全年销量最低的衣服
for i in data:
    if num > data[i]["数量"]:
        num = data[i]["数量"]
        name2 = i
    else:
        continue
print("全年销量最低的衣服是：",name2)