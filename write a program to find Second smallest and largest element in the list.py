#Second smallest and largest element in the list 
def find(list1):
    length=len(list1) 
    list1.sort()
    print("Second Largest element is:",list1[length-2])
    print('second smallest element is:',list1[1])
list1=[12,45,16,17,19,20]
Large=find(list1)
