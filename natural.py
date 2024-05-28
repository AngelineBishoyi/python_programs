f=open("demofile.txt","w")
f.write('the file has content')
f.close()
f=open("demofile.txt","r")
print(f.read())
#append data
f=open("demofile.txt","a")
f.write("\n Hello Naruto")
f.close()
f=open("demofile.txt","r")
print(f.read())

#print first character of the file
f=open("demofile.txt","r")
print(f.readline())
f.close()