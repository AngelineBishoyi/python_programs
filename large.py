def my_func(a1,b1):
    a1.extend(b1)
    b= a1.sort()
    return a1[-1]
a=[5,4,3,2,1]
b=[8,7,5,4,3,2]
fun=my_func(a,b)
print('Highest is',fun)