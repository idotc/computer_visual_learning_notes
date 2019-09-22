"""
输入数列个数
数列
3
1 5 2
5
1 5 233 7 8
"""
def predictWinner(n, nums):
    if n<3:
        return True
    dp = [[0 for _ in range(n)] for _ in range(n)]
    sum = 0
    for i in range(n):
        sum += nums[i]
        dp[i][i] = nums[i]
    for g in range(1, n):  # 间隔
        for i in range(n - g):
            j = i + g
            if g == 1:
                dp[i][j] = max(nums[i], nums[j])
            else:
                dp[i][j] = max(nums[i] + min(dp[i + 2][j], dp[i + 1][j - 1]),
                               nums[j] + min(dp[i][j - 2], dp[i + 1][j - 1]))
    return dp[0][-1] >= sum - dp[0][-1]
n = int(input())
nums = list(map(int, input().split()))
print (predictWinner(n, nums))