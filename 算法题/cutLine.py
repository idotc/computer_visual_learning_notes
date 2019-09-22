'''
背包问题
物品数量 背包容量
物品体积
物品价值
6 20
4 8 9 5 10 6
5 6 3 8 9 5
'''
# n, g = list(map(int, input().split()))
# space = list(map(int, input().split()))
# value = list(map(int, input().split()))
# dp = [0] * (g+1)
# for i in range(1, g+1):
#     for j, s in enumerate(space):
#         if (i-s) >= 0:
#             dp[i] = max(dp[i], dp[i-s]+value[j])
# print (dp[-1])

"""
剪绳子问题
绳子长度
20
"""
def maxCut(n):
    if n<2: return 0
    if n ==2 : return 1
    if n==3 : return 2
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    for i in range(1, n + 1):
        for j in range(1, i//2 + 1):
            dp[i] = max(dp[i], dp[j]*dp[i-j])
    return dp[-1]
n = int(input())
print (maxCut(n))

