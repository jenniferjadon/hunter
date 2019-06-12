g=int(input())
s=0
while g>0:
    d=g%10
    s=s+d**2
    g=g//10
print(s)
