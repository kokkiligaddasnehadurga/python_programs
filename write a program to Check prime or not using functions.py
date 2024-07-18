#Check prime or not using functions 
def prime(n):
    count=1
    for i in range(2, n+1): 
        if (n%i==0):
            count=count+1
    if(count>1):
        print("not a prime") 
    else:
        print("Prime")
prime(9)
