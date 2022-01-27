print("Loading the file")
f = open("test.txt")
print(f)
lines = f.readlines()
print(lines)

the_sum = 0

for line in lines:
    the_sum = the_sum + int(line)
print("The sum is",the_sum)

print("The sum is also",sum([int(x) for x in lines])) #prints the sum of the numbers in lines
