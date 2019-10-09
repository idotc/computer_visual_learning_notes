"""
题目：编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：
每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
输入：5，5，5  (行数，列数，查找目标值)
1,4,7,11,15
2,5,8,12,19
3,6,9,16,22
10,13,14,17,24
18,21,23,26,30
输出：True
"""

def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if not matrix:
        return False
    rows = len(matrix)
    cols = len(matrix[0])
    row = rows - 1
    col = 0
    while row >= 0 and col < cols:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            row -= 1
        elif matrix[row][col] < target:
            col += 1
    return False

rows, cols, target = list(map(int, input().split(',')))
matrix = []
for i in range(rows):
    matrix.append(list(map(int, input().split(','))))
print (searchMatrix(matrix, target))