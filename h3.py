m=int(input())
l=list(map(int,input().split()))
g=[]
c=0
for i in range(0,len(l)):
    if l[i]==i:
        c=c+1
        g.append(i)
if c>1:
    print(*g)
else:
    print("-1")
