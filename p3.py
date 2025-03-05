# 矩阵运算与快速幂的方法 最好 时间复杂度O(logn)

# 斐波那契数列
# 使用动态规划（自底向上）表格法
# 自底向上的方法是迭代方式，不使用递归，而是通过逐步计算从最小的子问题
# 每次计算时，将已经计算的结果存储在一个数组或表格中，确保每个子问题都只计算一次
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    dp = [0]*(n+1)
    dp[0]=0
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]

# 对上面的自底向上的算法进行空间优化
# 不用维持一整数组，仅保留前2个数
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
    
#     prev1, prev2 = 1, 0  # prev1代表F(n-1)，prev2代表F(n-2)
    
#     for i in range(2, n + 1):
#         current = prev1 + prev2  # 当前的F(i)是F(i-1) + F(i-2)
#         prev2 = prev1  # 更新prev2为prev1
#         prev1 = current  # 更新prev1为当前的值
    
#     return prev1

# 使用动态规划（自顶向下，带备忘录）
# def fib(n, memo={}):
#     if n in memo:
#         return memo[n]
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     memo[n] = fib(n-1, memo) + fib(n-2, memo)
#     return memo[n]

n=int(input())
print(fib(n))