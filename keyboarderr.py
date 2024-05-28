
print('Enter a string')
s=input()
upp=0
low=0
for i in s:
    if i.isupper():
        upp+=1
    else:
        low+=1
print('uppercase is',upp)
print('lowercase is',low)

