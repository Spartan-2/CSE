# Develop a python program to demonstrate handling of following exceptions using try and except. 
# NameError 
# IndexError 
# KeyError 
# ZeroDivisionError 


def handleExceptions():
    try:
        print(unknown_variable)
    except NameError as e:
        print("Name error ",e)
    
    try:
        list = [34,67,8]
        print(list[6])
    except IndexError as e:
        print("Index out of bounds ",e)
    
    try:
        dict = {"ty" : 74,
                67 : 789889,
                "op" : "oppp"}
        print(dict["iio"])
    except KeyError as e:
        print("Key error",e)
    try :
        i = 9
        print(i/0)
    except ZeroDivisionError as e:
        print("Zero Division error ",e)


handleExceptions()

        

