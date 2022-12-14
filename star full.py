i=1
while i<=5:
    print (" "*(5-i),end=" ")
    j=i
    while j<=i:
        print ("*",end=" ")
        j=j+1
    i=i+1
    print()
i=5
while i>1:
    print(" "*(6-i),end=" ")
    j=1
    while j<i:
        print("*",end=" ")
        j=j+1
    i=i-1
    print()            