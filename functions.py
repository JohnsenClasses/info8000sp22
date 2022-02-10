
from cmath import sqrt


def my_fun(to_print):
    print(to_print)
    return None
a = my_fun

c = 3+7.545345
print(c)
to_print = f"{c:.2f}"
a("hello world")
print(to_print)

def pyth(a,b=3,c=4):
    if b == None:
        b = a
    c2 = a**2+b**2
    return sqrt(c2)  

print(pyth(3,4))

def find(a_list,value):
    for i in range(0,len(a_list)):
        if a_list[i] == value:
            return (True,i)
    return (False,None)

a_list = [3,6,2]
found,index = find(a_list,8)
print(found,index)
print(pyth(3,c=4))


