#To implement permutation and combinations 
def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
n=int(input())
r=int(input())
per=fact(n)//(fact(n-r)*fact(r))
print(per)
