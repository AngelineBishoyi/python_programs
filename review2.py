def my_func(a):
    small=a[0]
    large=a[0]
    for i in a:
        if len(i)<len(small):
            small=i
        if len(i)>len(large):
            large=i
    return small,large
a=['a','cat','ballon','move','hat']
small,large=my_func(a)
print('Smallest is',small)
print('largest is',large)




a=['andie','cat','ballon',[12,32,8,5,8,3,9,7],'hat']
a.sort(key=len)
print( "The largest is",a[-1])
print("The smallest is",a[0])
a=[2,3,5,43,2,4,2,5]
b=[]
b=list(set(a))
print(b)
c=[]
c=b.remove(2)
print(c)