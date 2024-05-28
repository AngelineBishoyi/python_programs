def decoratorfun(func):
    def sumsquare(x,y):
        return func(x**2,y**2)
    return sumsquare
@decoratorfun
def add(a,b):
    return a+b
c=add(8,9)
print('sum is',c)