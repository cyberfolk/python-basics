import my_module as mm
import platform
import math
from my_module2 import persona2 # partial import
import datetime

x = mm.person1
x.greet("user0")

print(platform.system())    # windows
print(dir(math))
print(persona2)

# ***********************************************

x = datetime.datetime.now()

print(x)    # Base
print(x.strftime("%A %d %B %Y"))    # Formatted

# ***********************************************
