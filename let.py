'''song ="Let it go,Let it go,snowman......Let it go"
print(song.replace("Let","Dont let",2))
if (song.find("snowman")!=-1):
    print("Substring is present")
else:
    print("Substring is absent")

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common=list(set(list1)&set(list2))
print(common)'''
st='tutor joes'
'''l={}
for i in st:
    l[i]=l.get(i,0)+1
print(l)'''

for i in st:
    if st.count(i)>1:
        a=st.replace(i,'@',)
print(a)

st1=' Python'
f=st1[0]
l=None
for i in st1:
    i[-1]=i[0]
    print(st1)
