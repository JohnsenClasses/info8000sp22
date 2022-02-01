print("Loading the file")
f = open("data/test.txt")
print(f)
lines = f.readlines()
print(lines)
lines = [x.strip() for x in lines]
print(lines)

the_sum = 0

for line in lines: 
    the_sum = the_sum + int(line.strip())


print(f"The sum is {the_sum}")

print("The sum is also",sum([int(x) for x in lines])) #prints the sum of the numbers in lines


