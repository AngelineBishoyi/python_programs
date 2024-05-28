def duplicate(list):
    list1=[]
    for x in list:
        if x not in list:
             list1.append(x)
    return list1
list=[2,2,3,4,8,3,9,10]
b=duplicate(list)
print(b)