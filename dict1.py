'''d = {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}
for key in sorted(d.keys()):
    print(key, d[key])
    print(d.items())
    for k, v in d.items():
      print(k, '>', v)'''

#myDict = {'john' : [70, 82, 55], 'ram' : [92, 99, 98], 'jane' : [65, 34, 76]}
'''print( myDict)
sortedDict = {}
for value in sorted(myDict):
	sortedDict[value] = sorted(myDict[value])
print("Dictionary after sort of key and list value : ",sortedDict)'''
'''delkey=input('my key')
d=myDict.pop(delkey)
print(myDict)'''
myDict={"python" : 24, "C++" : 22, "javaScript" : 25, "Java" : 20, "R" : 21 }

sum=0
for value in myDict:
    sum=sum+myDict[value]

print(sum)

dic={'c++':2,'R':1}
for i in myDict:
    if i in dic:
        myDict[i]=dic[i]
print(myDict)