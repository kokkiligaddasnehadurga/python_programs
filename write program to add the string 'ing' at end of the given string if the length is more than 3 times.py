a=input("enter a string:")
b=len(a)
if(b>3):
    if a[-3: ]=='ing': 
        print(a+'ly')
    else:
        print(a+'ing')

else:
    print(a)
