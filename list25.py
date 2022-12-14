a=[4,6,4,3,3,4,3,4,3,8]
i=0
b=[]
count=0
while i<len(a)-1:
    k=a.count(a[i])
    if k>3:
        if a[i] not in b :
           b.append(a[i])
    i=i+1
print(b)    

