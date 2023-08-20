def greet(name="User"):
    print("Hello " + name)


def simple_sum(a, b):
    return a + b


def loop_sum(*operators):   # Arbitrary Arguments
    acc = 0
    for operator in operators:
        acc += operator
    return acc


greet("Raffaele")
print(simple_sum(1, 2))
print(simple_sum(1, 3))
print(simple_sum(1, 5))

print(loop_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, ))

# Arbitrary Keyword Arguments (todo)
