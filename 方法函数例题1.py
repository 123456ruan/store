'''
编写一个函数cacluate, 可以接收任意多个数,
返回的是一个元组.
元组的第一个值为所有参数的平均值,
 第二个值是大于平均值的所有数


函数的参数使用除了常规的位置参数和关键字参数外，
还支持可变个数的函数参数，这种支持可变个数的参数方法称为参数收集，对应的参数称为收集参数。
'''

def cacluate(*list):
    max = []
    ave = sum(list)/len(list)
    for i in list:
        if i > ave:
           max.append(i)
        else:
            continue
    tup = (ave,max)
    return tupi

print(cacluate(1,2,3,4,5,7,8,9))

