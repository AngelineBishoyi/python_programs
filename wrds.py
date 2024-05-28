no_of_wrds=0
with open(r'demofile.txt','r') as file:
    data=file.read()
    lines=data.split()
    no_of_wrds+=len(lines)
print(no_of_wrds)