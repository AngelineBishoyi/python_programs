#
'''def dict(num):
   
    s={i:i*i for i in range(1,num+1)}
    return s
num=8
print(dict(num))


# random sales dictionary
""sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

print(sales.values())


marks = {'Physics':67, 'Maths':87}

print(marks.items())'''
'''l=[1,2,3]
re=1
for i in l:
    re=re*i
print(re)

l=[1,9,8,7]
s=l[0]
l1=None
for i in l:
    if i>s:
        l1=s
        s=i
    elif l1 is None or i>l1:
        l1=i
print("second largest",l1)

A = {'Tamil': 92, 'English': 56, 'Maths': 88, 'Sceince': 97, 'Social': 89}
B= {'Tamil': 78, 'English': 68, 'Maths': 88, 'Sceince': 97, 'Social': 56}
for key,value in set(A.items())&(B.items()):
    print('%s %s is common in both dictionary' %(key,value))
count=0
Dict = { 'M1' : [67,79,90,73,36], 'M2' : [89,67,84], 'M3' : [82,57] }
for value in Dict.values():
    
    if isinstance(value,list):
        count=count+len(value)
        
print(count)
keys = ["One", "Two", "Three", "Four", "Five"]

values = [1, 2, 3, 4, 5]

a=dict(zip(keys,values))
print(a)

Dictionary = {'Name' : 'Ram', 'Age' : 23, 'City' : 'Salem', 'Gender' : 'Male', 'Mark' : 450}
keys = ["Name", "Age", "Mark"]
a={k:Dictionary[k] for k in keys}
print(a) '''

'''val = "Tutor joe's Computer Education"
print("Original string:", val)

dic = {"Computer": "Software", "Education": "Solution"}

word = val.split()
print(word)
res = []
for w in word:
    res.append(dic.get(w, w))
res = ' '.join(res)

print("Replaced Strings:", res)'''

re=[0,6,7,9,11,6,6,9,11]
l={}
count=0
for i in re:
   if  i in l:
      l[i]+=1
   else:
      l[i]=1
print(l)

R={'version':'1','subversion':'0.9','Metadata':{'submetadata':{'0':"yes",'1':'No','2':'male','3':'female'}}}
s=list(R['Metadata']['submetadata'].items())
print(s)
d=s[0],s[2],s[3]
print(list(d))
'''output = [R['Metadata']['submetadata']['0'], R['Metadata']['submetadata']['2'], R['Metadata']['submetadata']['3']]
print(output)'''

 
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
symbols = ['!', '@', '#']

a=zip(numbers,letters,symbols)
for i in a:
  print(i)
   



        