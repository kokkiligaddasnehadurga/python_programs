#Prime number in range 
def prime(x, y):
    list1=[]
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i%j == 0:
                    break
            else:
                list1.append(i)
    return list1
n=int(input())
m=int(input())
lst=prime(n,m)
if len(lst) == 0:
    print("There are no prime numbers in this range",lst)
else:
    print("The prime numbers in this range are: ", lst)
