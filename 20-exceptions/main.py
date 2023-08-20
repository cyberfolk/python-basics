try:
    print(0 / 0)
    print(x)    # If there is no try-except block the script aborts with NameError
except NameError:
    print("There was an NameError - X is not defined")
except ZeroDivisionError:
    print("There was an ZeroDivisionError")
else:
    print("No Problem")
finally:
    print("Finally")

# ***********************************************
x = -1
if x < 0:
    raise Exception("NegativeNumberExceptions")
