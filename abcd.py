n=int(input("no"))
i=1
v=ord("A")
while i<=n:
    j=1
    while j<=i:
        print(chr(v),end=" ")
        j=j+1
    print()
    k=1
    while k<=i:
        print("*",end=" ")
        k=k+1   
    i=i+1
    v=v+1
    print()    




# n=int(input("no"))
# i=1
# k=ord("A")
# while i<=n:
#     j=1
#     while j<=i:
#         if i%2!=0:
#            print(chr(k),end=" ")
#         if i%2==0:
#             print(i,end=" ")
#         j=j+1
#     k=k+1
#     i=i+1
#     print()   

 