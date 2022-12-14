a=[[0],[1,3],[5,7],[9,11],[13,15,17]]
i=0
max=0
min=1000
while i<len(a):
    h=len(a[i])
    if h>max:
        max=h
        g=a[i]
    if h<min:
        min=h
        f=a[i]
    i=i+1
print(max,[g])
print(min,[f])        

                 
