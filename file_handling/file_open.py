
# open("file_name" ,"Mode")
#  r= read
#  w = write
 


file = open("data.txt","r")

# content = file.read()
# data=file.readlines() return the list
# data=file.read() return the all text in same formate String
data=file.readline() #return the single line
 

# data=file.read()

print(data)
print(type(data))

file.close()