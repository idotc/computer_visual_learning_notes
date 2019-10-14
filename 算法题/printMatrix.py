'''
题目：顺时针螺旋打印矩阵
输入：
行 列
矩阵
3 3
1 2 3
4 5 6
7 8 9
输出：
1,2,3,6,9,8,7,4,5
'''
def printMatrix(matrix):
    """
        :type matrix: list[list]
        :rtype: out: list
    """
    out = []
    while matrix:
        out += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                out.append(row.pop())
        if matrix:
            out += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                out.append(row.pop(0))
    return [str(i) for i in out]

rows, cols = list(map(int, input().split()))
mat = []
for _ in range(rows):
    mat.append(list(map(int, input().split())))
print (','.join(printMatrix(mat)))