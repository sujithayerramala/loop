a=[6,1,3,5,6,3,1]
i=0
b=[]
p=1
while i<len(a):
    if a[i] not in b:
        b.append (a[i])
print(b)
p=1
i=0 
while i<len(b):
    p=p*a[i]
    i=i+1
print(p)                   