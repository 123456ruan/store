'''
用三个列表表示三门学科的选课学生姓名(一个学生可以同时选多门课)
语文 = ['小明','小张','小黄','小杨']
数学 = ['小黄','小李','小王','小杨','小周']
英语 = ['小杨','小张','小吴','小冯','小周']
1)求选课学生总共有多少人
2)求只选了第一个学科的人的数量和对应的名字
3)求只选了一门学科的学生的数量和对应的名字
'''
chinese = ['小明','小张','小黄','小杨']
math = ['小黄','小李','小王','小杨','小周']
english = ['小杨','小张','小吴','小冯','小周']
sum1 = chinese + math +english
# 1求选课学生总共有多少人
sum2 =[]
for i in range(len(sum1)):
    if sum1[i] not in sum2:
        sum2.append(sum1[i])
    else:
        continue
print("选课学生总共有：",len(sum2))
print(sum2)

# 2.求只选了第一个学科的人的数量和对应的名字
print("只选了第一个学科的人的数量:",len(chinese))
print(chinese)
# 3.求只选了一门学科的学生的数量和对应的名字
n = 0
sum3 = []
for i in range(len(sum1)):
    if sum1.count(sum1[i]) == 1:
        n = n + 1
        sum3.append(sum1[i])
print("选了一门学科的学生总共:",n)
print(sum3)
