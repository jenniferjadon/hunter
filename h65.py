h,n=map(int,input().split())
m=list(map(int,input().split()))
while n in m:
    m.remove(n)
if not m:
    print("empty")
else:
    print(*m)
