b=int(input())
f=list(map(int,input().split()))
d=sorted(f)
s=d[::-1]
for i  in range(0,len(s)):
    print(s[i],end="")
