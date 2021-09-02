import time
while True:
    data =  open(file="baidu_x_system.log",mode="r+",encoding="utf-8").readlines()
    data1 = []
    sum = {}
    for i in data:
        data1.append(i.split(" "))
    for i in range(len(data1)):
        if data1[i][0] in sum:
           sum[data1[i][0]] = sum[data1[i][0]]+1
        else:
            sum[data1[i][0]] = 1
    print(sum)
    time.sleep(6)
