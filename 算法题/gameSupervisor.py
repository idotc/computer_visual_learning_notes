"""
题目：每轮游戏都要有一个人当裁判,其余n-1个人当玩家
给出每个人想当玩家的次数ai
请你求出所需要最少的玩游戏的轮数
使得每个人都能满足他们当玩家的要求.
"""
n = int(input())
nums = list(map(int, input().split()))
ans = 0
sum = sum(nums)
if sum % (n-1) == 0:
    ans = sum//(n-1)
else:
    ans = sum//(n-1) + 1
ans = max(ans, max(nums))
print (ans)