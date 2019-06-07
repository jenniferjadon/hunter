g=int(input())
f=list(map(int,input().split()))
c=0
for i in range(0,len(f)):
    for j in range(i+1,len(f)):
        if f[i]+f[j]==0:
            print(f[i],f[j])
