f=open('demofile.txt')
lines=[]
for i in f:
    lines.append(i.split())
print(lines)