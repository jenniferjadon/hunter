j=input()
d=j.replace(" ","")
g=''
for i in range(1,len(d)+1):
    if i%2==1:
        g=g+d[i-1].upper()
        #print(g)
    else:
        g=g+d[i-1]
        #print(g)
for i in range(0,len(j)):
    if j[i]==" ":
        g=g[0:i]+" "+g[i::]
print(g)
        
