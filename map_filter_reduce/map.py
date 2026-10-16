# import math as mt
# list=[1,2,3,4]
# #  map(function , iterabel)
# def squre(x):
#     return x**2
# squre_list=map(squre,list)
# for x in squre_list:
#     print(x)


# squrert=map(lambda x:mt.sqrt(x),list )
# for x in squrert:
#     print(x)

a=[1,10,3]
b=[4,5,6]
List_Sum=map(lambda x,y:x+y, a,b)

print(list(List_Sum))