h,n=map(int,input().split())
m=list(map(int,input().split()))
a=[]
if len(m)==0:
    print("empty")
for i in m:
    if i!=n:
        a.append(i)
print(*a)
   
