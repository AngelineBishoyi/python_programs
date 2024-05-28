def occurence(str,char):
    count=0
    for c in str:
        if c ==char:
            count+=1
    return count
str='Glorious'
char='o'
occ=occurence(str,char)
print(f'Te character {char} appears {occ} times')
