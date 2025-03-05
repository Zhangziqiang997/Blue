# 爬楼梯问题
# 假设有一个楼梯共 n 阶，你每次可以选择爬 1 阶或 2 阶。
# 问：你有多少种不同的方法可以爬到第 n 阶？

# def climbStairs(n):
#     if n==0 or n==1:
#         return 1
#     dp = [0] * (n + 1)  # 初始换dp数组
#     dp[0] = 1
#     dp[1] = 1

#     for i in range(2,n+1):
#         dp[i] = dp[i - 1] + dp[i - 2]   # 状态转移方程

#     return dp[n]

# 优化空间
def climbStairs(n):
    if n==0 or n==1:
        return 1
    dp1,dp2 = 1, 1
    for i in range(2,n+1):
        current = dp1+dp2
        dp1 = dp2
        dp2 = current
    return dp2

n=int(input())
print(climbStairs(n))