# l=[10,20,80,90,100]
# l.sort()
# print(l)
# print("first maximum:",l[-1])
# print("second maximum;",l[-2])
# print("third maximum:",l[-3])


h=[1000,2,11,15,8,4,41,8]
i=0
m1=0
m2=0
m3=0
while i<len(h):
    if h[i]>m1:
        m1=h[i]
    i=i+1 
    j=0
    while j<len(h):
        if h[j]>m2 and h[j<m1]:
            max2=h[j]
        j+=1
    k=0
    while k<len(h):
        if h[k]>m3 and h[k] <m2:
            m3=h[k]
        k+=1
print ("max1")
print ("max2")
print ("max3")

      






 