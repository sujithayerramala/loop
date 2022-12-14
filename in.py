# a="abcdefghijklmnopqrstuvwxyz"
# i=0
# b=int(input("enter the number"))
# while i<len(a):
#     j=i
#     while j<i+b:
#         print(a[j],end=" ")
#         j+=1
#     i+=5
#     print()

     

# a=[2,3,5,6,9]
# a.insert(3,12)
# print (a)   



a=int(input("enter the year"))
b=int(input("enter the month"))
c=int(input("enter the date"))
if a>0:
    if b>=1 and b<=12:
        if c>=1 and c<=30:
            print(c+1,b,a)
        else:
            print("1",b+1,a)
    else:
        print("enter valid data")           