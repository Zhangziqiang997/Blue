
n,d,k = map(int,input().split())

ar = []
for _ in range(n):
    a,b = map(int,input().split())
    # a,b = input().split()
    ar.append((a,b))

ar.sort(key = lambda x: (x [1] ,x[0]))
# ci = ar[0][1] # 当前遍历的帖子
ci=-1
like_post = []
for i in range(len(ar)):
    if ci != ar[i][1]:
        ci=ar[i][1]
        # 进入下一个帖子的遍历
        i_start = i
        start = ar[i_start][0]
        current = ar[i][0]
        like = 1
    else:
        if ci in like_post:
            continue
        current = ar[i][0]
        if current - start < d:
            like += 1
        else:
            i_start += 1
            start = ar[i_start][0]
        if like >= k:
            like_post.append(ci)

for i in sorted(like_post):
    # print(i)
    # print(i)

       

