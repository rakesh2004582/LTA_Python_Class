#  empty list append , slicing , indexig , also nagativ

# list=[]
# # print(len(list))
# list.append(1)
# list.append(2)
# list.append(3)
# list.append(4)
# list.append(5)
# list.append(6)
# # print(len(list))
# # print(list)
# print(list)
# slice1=list[0::2]
# print(slice1)
# reverse_list=list[-1:-5:-1]
# print(reverse_list)
# #===================
# # 0  1   2  3   4
# #[3, 4, 6, 7, 8]
# #-5 -4 -3 -2  -1

# extend

# list1=[1,2]
# list2=[3,4]
# # list1.append(list2)
# print(list1,len(list1))
# list1.extend(list2)
# print(list1)
# print("len : ",len(list1))


# insert, index

# list=[1,2,3,4]
# list.insert(0,9)
# print(list)
# print(list.index(8))

# remove ,pop ,clear
# list=[2,3,4,6,43,4,7]
# print(list)
# list.remove(4)
# print(list)
# list.remove(4)
# print(list)
# print(list.pop())
# print(list)
# list.clear()
# print(list)

# count, sort, reverse

# list=[2,4,2,4,6,4,7,3,2,3,6,4,2,3]
# print(list.count(2))
# list.sort()
# print(list)
# list.reverse()
# print(list)


# copy 
# a=[1,2,3,4]
# b=a
# print(a)
# print(b)
# b[0]=100
# print(a)
# print(b)
# c=a.copy()
# c[0]=200
# print(a)
# print(c)


# sorted
list=[2,8,1,3]
sorted_list=sorted(list)
print(sorted_list)
print(list)
