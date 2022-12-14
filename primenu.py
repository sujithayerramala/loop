a=int(input("enter the number"))
i=1
while i<=a:
    j=1
    v=0
    while j<=i:
        if i%j==0:
            v=v+1
        j=j+1    
    if v==2:
        print(i)
    i=i+1    
                  

