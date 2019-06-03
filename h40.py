j=str(input())
s=0
for i in j:
    s=s+int(i)
if str(s)==str(s)[::-1]:
    print("YES")
else:
    print("NO")
