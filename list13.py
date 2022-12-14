a=[1,1,2,3,4,4,5,1]
b=[]
i=0
while i<len(a)-1:
    count=1
    if a[i]==a[i+1]:
        count+=1
        d=[count,a[i]]
        b.append(d)
        i+=1
    else:
        b.append(a[i])
    i=i+1
b.append(a[-1])
print(b)            

