try:
    try:
        print(10/0)
    except Exception as a:
        print(a)
    try:
        list=[34]
        x=list[8]
    except Exception as a:
        print(a)
    print(10/0)
except Exception as a:
    print(a)