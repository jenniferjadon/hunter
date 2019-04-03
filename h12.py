m,n=list(map(int,input().split()))
h=list(map(int,input().split()))
h=sorted(h)
k=h[::-1]
print(k[n-1])
