'''
编写函数, 接收一个列表和一个索引，
返回这个列表中对应索引的数据，
如果索引超出范围，返回-1.
'''

def realization(list, n):
    if n >= len(list) or n < 0:
        return -1
    else:
        return list[n]


list = [1,2,3,4,5,"147852",7,8,9]
print(realization(list,-8))