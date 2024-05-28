list1 = [5, 10, 15, 20, 25, 50, 20]
#while 20 in list1:
      #a=list1.index(20)
      #list1[a]=200
for i in list1:
      if (i==20):
            list1.remove(i)      
print(list1)

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
if isinstance(list1[-1],str):
      list1[-1]=[list1[-1]]
list1[-1].append(sub_list) 
print(list1)  


list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)


list1 = ["Mike", [], "Emma", "Kelly", [], "Brad"]
while [] in list1:
      list1.remove([])
print(list1)

list1 = [10, 20, 30, 40]
list2 = [100,200,300,400]

a= zip(list1,list2)
print(dict(a))

numbers = [1, 2, 3, 4, 5, 6, 7]
num=[]
for i in numbers:
      num.append(i*i)
print(num)

lis1 = ["M", "na", "i", "Ke"]
lis2 = ["y", "me", "s", "lly"]
lis3 = [x+y for x,y in zip(lis1,lis2)]
print(lis3)

list1=[2,4,3,34,54,3,2,3]
for i in range(len(list1)):
     for j in range(i+1,len(list1)):
          if list1[i] < list1[j]:
             list1[i],list1[j]=list1[j],list1[i]
print(list1)