from vector import Vector
a_list = [3.23423,4]
a_vec = Vector(a_list.copy())
b_vec = Vector([4,5])
print(str(a_vec))
print(len(a_vec))
print(a_vec.length())

print(Vector.__len__(a_vec))

try:
    c_vec = Vector(["a","b"])
    print(Vector.length(c_vec))
    print(c_vec.length())
except:
    print("failed to create valid vector")
print(a_vec+b_vec)
d_vec = a_vec.copy()
print(d_vec)
d_vec[0] = 90
print(d_vec)


