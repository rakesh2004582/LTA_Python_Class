list=[1,3,5,7,9]
squre=lambda x:x%2==0

squre_list=[squre(x) for x in list]
print(squre_list)