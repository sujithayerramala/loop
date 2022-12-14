# a=int(input("enter the number"))
# b=int(input("enter the number"))
# i=1
# sum=0
# while i<=b:
#     sum=sum+a
#     i=i+1
#     print(sum)



i=1
while i<=20:
    if i%3==0 and i%5==0:
        print("i love you")
    elif i%3==0:
        print("i")
    elif i%5==0:
        print("love")
    else:
        print("no")
    i=i+1                