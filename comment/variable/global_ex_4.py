x = "awesome"


def myFunc():
    global x
    print ("python is "+ x)
    x = "fantastic"

myFunc()
print ("python is "+ x)
