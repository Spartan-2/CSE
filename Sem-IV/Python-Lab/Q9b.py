# Develop a python program to demonstrate handling multiple exceptions using try, except, else and finally block statements

def multipleException():
    try:
        i = 90
        print(i/0)
    except ZeroDivisionError as e:
        print(e)
    except NameError as e:
        print(e)
    except:
        print(e)
    finally:
        print("Finally is executed")

multipleException()
