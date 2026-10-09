import csv

# with open("student.csv","r") as file:
#     rows=csv.reader(file)
#     first= next(rows)
#     print("this is the header of file  : ",first)
#     for row in rows:
#         print(row)

# with open("student.csv","r") as file:
#     dict_data=csv.DictReader(file)
#     print(dict_data)
#     # for d in dict_data:
#     #     print(d)
#     print(next(dict_data))

data=[
    ["name","age","city","MOb"],
    ["Aman",21,"Kashganj",9868686],
    ["raman",33,"etha",1234]
    ]

with open("dummydata.csv","w") as file:
    # writer=csv.writer(file)
    # writer.writerows
    # csv.writer(file).writerows(data)
    write=csv.writer(file)
    # write.writerow(data[0])
    write.writerow(["name","age","city"])