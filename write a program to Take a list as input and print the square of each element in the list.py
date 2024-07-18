#Take a list as input and print the square of each element in the list 
def squarenum(list1):
    list2=[]
    for i in list1:
        list2.append(i**2)
    print(list2)
squarenum([2,4,6])
