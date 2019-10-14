"""
题目：不能使用可以函数，求一个数的平方根，保留四位小数
输入：
2
输出：
1.4142
"""
def sqrtNumber(num):
    """
     :type num: int
     :rtype: result: float
    """
    result = 1
    while (result - num/result)> 1e-8 or (result - num/result)< -(1e-8):
        result = (result + num/result)/2
    return result

num = int(input())
print ("%0.4f" % sqrtNumber(num))