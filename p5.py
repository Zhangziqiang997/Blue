'''
有一个密室逃脱游戏,有100间密室连在一排。
密室编号是从1开始连续排列一直排到第100间密室。
游戏规则:
1.玩家初始位置在1号密室;
2.每次玩家可以进入右边的一个密室，也可以跳过一个密室进入下个密室
(如:当玩家当前在3号密室他可以进入4号密室也可以进入5号密室)；
编程实现:给定三个正整数X,Y,M(X<Y<M≤100)，表示三个密室编号。
X号密室和Y号密室有毒气泄漏,不能进入,玩家需要进入到M号密室。按
照游戏规则进入M号密室有多少种路线方案。例如:X=2,Y=4,M=7 
进入M号密室有2种路线方案,分别是1->3->5->6->7路线和1->3->5->7路线。
'''
def f(x,y,m):
    if x==2 and y==3:
        return 0
    dp=[0]*(m+1)
    dp[1]=1
    if x == 2:
        dp[2]=0
    else:
        dp[2]=1
    
    for i in range(3,m+1):
        if x == i or y == i:
            dp[i] = 0
        else:
            dp[i] = dp[i-1]+dp[i-2]
    #还可以进一步优化空间
    return dp[m]
x,y,m = map(int,input().split(','))
print(f(x,y,m))