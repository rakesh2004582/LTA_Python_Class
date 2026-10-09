import json
# from json import load
# with open("user.json","r") as f:
#     load_data=json.load(f)
#     print(load_data["name"])

file =open("user.json","r")
load_data=json.load(file)

print(load_data["name"])
file.close()
