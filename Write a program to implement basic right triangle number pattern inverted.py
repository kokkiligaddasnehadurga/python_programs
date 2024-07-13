n=int(input())
count=0
for i in range(n,0,-1): 
    count=count+i 
for i in range(0,n):
    for j in range(0,n-i): 
        print(count, end=" ") 
        count=count-1
    print()
