file=input('Enter File: ')
fh = open(file, "r")

count = 0
for line in fh:
    print(line.strip())
    count = count + 1

print(count,"Lines")
