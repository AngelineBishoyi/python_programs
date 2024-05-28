def my_func(list1):
    newlist=[]
    duplist=[]
    for i in list1:
        if i not in newlist and i not in duplist:
             newlist.append(i) 
        else:
            newlist.remove(i)
            duplist.append(i)
    return duplist,newlist,len(duplist),len(newlist)
lis1=[5,3,6,7,5,3,8,9]
duplicates,non_duplicates,count_duplicates,count_nonduplicates=my_func(lis1)
print('duplicates',duplicates)
print('non duplicates',non_duplicates)
print('count of duplicats',count_duplicates)
print('count of non duplicates',count_nonduplicates)

