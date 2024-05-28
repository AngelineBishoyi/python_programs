def vowel(str):
    result=''
    vow=('a','e','i','o','u')
    for x in str:
        if x not in vow:
            result+=x
    return result
str='Chosen'
ch=vowel(str)
print(ch)