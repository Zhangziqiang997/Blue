"""
矩形拼接
已知 3 个矩形的大小依次是 a1 × b1, a2 × b2 和 a3 × b3。
用这 3 个矩形能拼出的所有多边形中，边数最少可以是多少？
输入格式
输入包含多组数据。

第一行包含一个整数 T，代表数据组数。

以下 T 行，每行包含 6 个整数 a1, b1, a2, b2, a3, b3，其中 a1, b1 是第一个矩形的边长，a2, b2 是第二个矩形的边长，a3, b3 是第三个矩形的边长。

输出格式
对于每组数据，输出一个整数代表答案。
样例输入
2
2 3 4 1 2 4
1 2 3 4 5 6
样例输出
4
6
"""
# 情况2：完全匹配条件：三个矩形中有前两个矩形的边等于第三个矩形的边，而且前两个矩形的另一条边相等
def check1(x1,x2,x3):           # 完全匹配：四边形
    if x1>=x2 and x1>=x3:#当x1是最大的边时，后续判断两个短的边加起来是否等于长边，并且判断两个小矩形的另一条边相等
        if x1==x2+x3 and a[2]+a[3]-x2==a[4]+a[5]-x3:return True#两个短边位置可以确定在23中一个，45中一个，
    if x2>=x1 and x2>=x3:#当x2是最大的边时
        if x2==x1+x3 and a[0]+a[1]-x1==a[4]+a[5]-x3:return True#比较两个短边的另一条边：把两个短边加起来减去已知的剩下的就是另一条边
    if x3>=x1 and x3>=x2:#当x3是最大的边时
        if x3==x1+x2 and a[0]+a[1]-x1==a[2]+a[3]-x2:return True
    return False
#情况3
def check2( x1,x2,x3):          # 部分匹配：六边形
    if x1>=x2 and x1>=x3:
        if x1==x2+x3:return True # 这里不需要判断前两个矩形另一边不相等，因为check1()函数已经选出了相等的，所以剩下的都是不相等的
    if x2>=x1 and x2>=x3:
        if x2==x1+x3:return True
    if x3>=x1 and x3>=x2:
        if x3==x1+x2:
            return True
    return False
T = int( input())                     # 读取T组测试
for t in range(T):
    a=list(map(int,input().split()))  # 读取三个矩形的长和宽
    ans=8                          # 最大的边数（最差的结果）
    for i in range(0,2):           # 取第1个矩阵的边
        for j in range( 2,4):      # 取第2个矩阵的边
            for k in range(4,6):   # 取第3个矩阵的边
                x1,x2,x3 = a[i],a[j],a[k]       # x1,x2,x3是三个矩形的一边，6种组合
                if x1==x2 and x2==x3:   # 情况1：三个矩形有一边相等
                    ans = min(ans,4)
                if check1(x1,x2,x3):#情况2：三个矩形中有前两个矩形的边等于第三个矩形的边，而且前两个矩形的另一条边相等
                    ans = min(ans,4)
                if x1==x2 or x1==x3 or x2==x3:#情况4：如果有两个矩阵有一条边相等，那么合并后就是6条边
                    ans = min(ans,6)
                if check2(x1,x2,x3):#情况3：三个矩形中有前两个矩形的边等于第三个矩形的边，而且前两个矩形的另一条边不相等
                    ans = min(ans,6)
    print(ans)
