n=int(input())
a=list(map(int,input().split()))
b=[]
c=0
for i in a:
    if i not in b:
        b.append(i)
    else:
        c=c+1
        break
if c==0:
    print("unique")
else:
    print(i)
