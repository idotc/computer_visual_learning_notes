"""
题目：递推数列满足规则：a[n] = a[n-1] + a[n-3] + a[n-4]
输入数列为：nums
求第n位的数
要求复杂度为： nlogn
"""
def mul(a, b):  # 首先定义二阶矩阵乘法运算
    row = len(a)
    col = len(a[0])
    c = [[0 for i in range(col)] for j in range(row)]  # 单位矩阵，等价于1  # 定义一个空的二阶矩阵，存储结果
    for i in range(row):  # row
        for j in range(col):  # col
            for k in range(col):  # 新二阶矩阵的值计算
                c[i][j] += a[i][k] * b[k][j]
    return c

def quickMatMul(mat, n):
    row = len(mat)
    col = len(mat[0])
    res = [[1 if i==j else 0 for i in range(col)] for j in range(row)] # 单位矩阵，等价于1
    while n:
        if n & 1: res = mul(res, mat)  # 如果n是奇数，或者直到n=1停止条件
        mat = mul(mat, mat)  # 快速幂
        n >>= 1  # 整除2，向下取整
    return res

A = [[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [1, 1, 0, 1]]
n = 20
nums = [1, 2, 3, 4]
weight = quickMatMul(A, n-len(nums))[-1]
result = 0
for i in range(len(nums)):
    result += weight[i] * nums[i]
print (result)
