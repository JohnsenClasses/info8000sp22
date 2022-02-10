a_list = [0,13,95,34,56,12]
a_list.reverse()
print(a_list)

#a_list.reverse()

a_list.sort()

print(sorted(a_list))

print(a_list)

a_list.append(7)

print(a_list)

a_list.extend([53,27])

print(a_list)

a_list.append([342,234])
print(a_list)

a_list.pop() #removes the last item (and technically returns it)

print(a_list)

a_list.remove(95) #removes the object 95

print(a_list)

del a_list[3] #deletes the 3rd element

print(a_list)

a_list = a_list[0:3] #removes all but the first 3 elements

print(a_list)

a_list.insert(2,3)
print(a_list)


#finding the deltas for an integer list

a_list = [3,5,7,10,1,6]


for second_num in a_list[1::2]:
    print(second_num)


deltas = []
for i in range(1,len(a_list)):
    deltas.append(a_list[i] - a_list[i-1])


print(deltas)

a = [3,1,1]
b = [7,8,9]
c = a-b
print(c)