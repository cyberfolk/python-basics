import my_module as mm
import platform
import math
from my_module2 import persona2 # partial import

x = mm.person1
x.greet("user0")

print(platform.system())    # windows
print(dir(math))
print(persona2)
