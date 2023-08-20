x = "X - outside the function"  # Global scope


def print_x():
    x = "X - inside the function"   # Function scope
    print(x)


def print_x_global():
    global x
    print(x + " (global)")


print(x)
print_x()  # print the x inside the function
print_x_global()  # use global to print the x outside de function
