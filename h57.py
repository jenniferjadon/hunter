h=int(input())
d=list(map(int,input().split()))
g=[]
for i in d:
    if d.count(i)==1:
        g.append(i)
print(*g)
