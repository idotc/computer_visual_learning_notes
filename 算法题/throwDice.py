"""
题目：掷n个不同面数的骰子，以最大点数为结果，求点数的期望。一共有n个骰子第i个骰子面数为ni，点数为[1,ni]，每个面的概率相同同时掷这n个骰子，所有骰子中的最大点数为最终点数求骰子投出的期望值。
输入：骰子的个数
点数
2
2 2
输出：期望值
1.75
"""
n = int(input())
dice = list(map(int, input().split()))
dice.sort(reverse=True)
res = [0]
cur = [0]
for _ in range(dice[0]):
    res.append(1/dice[0])
    cur.append(1/dice[0])
for i in range(1, n):
    for j in range(1, dice[i]+1):
        a = sum(res[:j])*(1/dice[i]) #a表示之前骰子的值小于j，而当前骰子的值等于j
        b = res[j] * (1/dice[i]) #b表示之前骰子的值等于j，而当前骰子的值也等于j
        c = res[j] * ((j-1)/dice[i]) #c表示之前骰子的值等于j，而当前骰子的值小于j
        cur[j] = a + b + c #更新当前期望取 j 时的概率
    res = cur[:]
ans = 0
for i in range(1,len(res)):
    ans += i*res[i]#求期望
print (ans)