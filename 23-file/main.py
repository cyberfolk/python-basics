f = open("text.txt", "r")
# print(f.read())  #  Read the entire file
# print(f.read(5))  # Read 5 char

print("SINGLE READ")
print(f.readline())  # Read a single line, the next call of this method read the next line

print("READ WITH LOOP")
for row in f:
    print(row)
f.close()
# print(f.readline())  # ValueError

# *** APPEND *************************************
# Append to EOF

f = open("text.txt", "a")
f.write("WRITED LINE")
# print(f.readline())  # io.UnsupportedOperation

# *** WRITE *************************************
# Overwrite the file

f = open("text.txt", "w")
f.write("WRITED LINE")

# ***********************************************





