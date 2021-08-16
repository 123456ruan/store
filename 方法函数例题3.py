'''
不使用for或者while循环，
就使用方法完成1~150之间的数的打印。（方法的递归调用）
'''


def printNum(num):

    if num <= 150:
        print(num, end="\t")
        num = num + 1
        printNum(num)
printNum(1)
