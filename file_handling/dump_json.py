import json

dict={
    "Aditya":55,
    "namesh":33,
    "asheesh":55,
}

with open("Student.json","w") as f:
    json.dump(dict,f)