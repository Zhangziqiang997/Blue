'''
水仙花
输入一个整数N,判断100到N之间有多少个水仙花数

输入160
输出1

'''

def flower(N):
    a=int(N/100)
    b=int(N/10%10)
    c=int(N%10)
    #整除运算符 //
    # a=N//100
    # b=(N//10)%10
    # c=N%10
    if a**3+b**3+c**3 == N:
        return True
    else:
        return False
    #return a**3 + b**3 + c**3 == N

N=int(input())
cnt=0
for i in range(100,N+1):
    if flower(i):
        cnt+=1
print(cnt)