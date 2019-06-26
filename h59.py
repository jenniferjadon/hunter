h=int(input())
d=list(map(int,input().split()))
h=list(map(int,input().split()))
a=[]
for i in range(0,len(d)):
        s=d[i]+h[i]
        a.append(s)
print(*a)
