a=[1, 2, 0, 3, 0, 4, 0, 5]

j=0
for i in range(len(a)):
    if a[i]!=0:
        a[j],a[i]=a[i],a[j]
        j+=1
print(a)


 

         