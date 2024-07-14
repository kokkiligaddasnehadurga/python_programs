#Maximum of 3 numbers using functions
def maximum(a,b,c):
    if(a>b and a>c):
        print(a)
    elif (b>a and b>c):
        print(b)
    else:
        print(c)
maximum(10,20,30)
