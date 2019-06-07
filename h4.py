g=int(input())
f=list(map(int,input().split()))
for i in f:
    if(f.count(i)==1):
        print(i)
