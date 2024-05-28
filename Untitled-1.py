list1=[5,3,5,6,3,7,8,9]
newlist=[]
duplist=[]
for i in list1:
    if i not in newlist:
        newlist.append(i)
    else:
            duplist.append(i)
print('Duplicates', duplist)
print('Non duplicates', newlist)
print('count of diplicates',len(duplist))
print('count of non duplicates',len(newlist))