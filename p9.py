s=input()
count=0
com=""
for i in range(1,len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        if count>1:
            com += s[i-1] +str(count)
        else:
            com += s[i-1]
        count = 1
if count>1:
    com += s[-1] +str(count)
else:
    com += s[-1] 

if len(com) < len(s):
    print(com)
else:
    print("NO")