#Take the input string count no.of uppercase and lowercase letters
def countupper(s):
    upper=0
    lower=0
    for i in s:
        if(i>='A' and i<='Z'):
            upper+=1 
        elif(i>='a' and i<='z'): 
            lower+=1
    print('upper is',upper)
    print('Lower is',lower)
countupper('PyThOn')
