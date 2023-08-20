f = open("text.txt", "r")

print("TEXT.TEXT")
print(f.read())  # Print the entire file
f.close()

new_row = input("> Write the contents of the new line? ")
pos_row = int(input("> Write the position of the new line: "))
num_rows = sum(1 for _ in open("text.txt"))  # Read and count num_row
i = 0

fr = open("text.txt", "r")
fw = open("out.txt", "w")

for row in fr:
    i += 1
    if i == pos_row:
        fw.write(new_row + "\n")
    fw.write(row)

fr.close()
fw.close()
