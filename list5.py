l=[1,2,2,5,8,4,4,8]
i=0
b=[]
while i<len(l):
    c=l[i]
    if l[i] not in b:
        b.append (l[i])
    i=i+1
print(b)       
        
