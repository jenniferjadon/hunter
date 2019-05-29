k,m=list(map(str,input().split()))
p=[]
for i in k:
    for j in m:
        if i==j:
            p.append(i)
    print("yes")
    break
else:
    print("no")
