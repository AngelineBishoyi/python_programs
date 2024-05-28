def ascending(list):
    for i  in range(len(list)):
        if list[i]>list[i+1]:
            print('sorted')
        else:
            print('not sorted')
            
list=[3,4,9,7,10]
b=ascending(list)
print(b)