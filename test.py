print("Loading the file")
f = open("test.txt")
print(f)
lines = f.readlines()
print(lines)

the_sum = 0

for line in lines:
    the_sum = the_sum + int(line)
    print(the_sum)

print(sum([int(x) for x in lines])) #prints the sum of the numbers in lines
