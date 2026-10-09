id="LTA12"
password="abc123"

def login(id,password):
    if id=="LTA12":
        print("user get")
        if password=="abc123":
            print("password match ..")
            print("login done!")
        else:
            raise Exception("password not found ")
    else:
        raise Exception("User not fount exception ")

try:
    login( id,"password")
except Exception as a:
    print(a)
else:
    print("welcome to dashboard ")
finally:
    print("program executed ...")