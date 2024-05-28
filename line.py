
f=open("demofile.txt","a")
f.write("\n   Hope you are enjoying learning python")

srch_txt="Naruto"
rplc_txt="Itachi"

with open(r'demofile.txt','r') as file:
    data=file.read()
    data=data.replace(srch_txt,rplc_txt)
with open(r'demofile.txt','w') as file:
    file.write(data)
print('text replaces')