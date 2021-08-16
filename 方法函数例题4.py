'''
同样使用方法的递归，求1~300所有数的和。
'''

sum = 0
def printNum(num):
    # sum = 0
    global sum
    if num <= 300:
        sum = sum + num
        num = num + 1
        printNum(num)
printNum(1)
print("总和为:",sum)