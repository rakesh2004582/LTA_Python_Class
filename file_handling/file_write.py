
list=["line 1\n","line 2\n","line 3\n","lin 4\n"]
file = open("data1.txt","w")
file.writelines(list)
 
file.close()


file = open("data1.txt","r")

print(file.tell())
cont=file.readline()
print(cont)
print(file.tell())
file.seek(0)
cont=file.readline()
print(cont)
print(file.tell())

file.close()