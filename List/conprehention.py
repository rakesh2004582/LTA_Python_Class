# list=[1,2,3,4,5]

# squre=[x**2 for x in list]
# print(squre)
# add10=[x+10 for x in list]
# print(add10)

# bool_list=[True if x%2==0 else False for x in list]
# second=[x%2==0 for x in list]
# print(second)

list=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


bool_list=[col%2==0 for row in list for col in row ]
print(bool_list)

squre=[x**2 for row in list for x in row]
print(squre)