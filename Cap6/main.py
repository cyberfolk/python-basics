i = 0
END = 100
while i < END:
    i += 1
    if i == 5:
        continue    # skip to next iteration
    if i == 10:
        break   # stop cycle
    print(i)
else:
    print("End while")
