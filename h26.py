m=int(input())
v=list(map(int,input().split()))
f=[]
for i in v:
    f.append(i)
f=f[::-1]
print(*f,sep="->")
