list1=[12,35,9,56,24]
def swaplist(list1,pos1,pos2):
    list1[pos1],list1[pos2]=list1[pos2],list1[pos1] 
    return list1
pos1=int(input())
pos2=int(input())
print(swaplist(list1,pos1,pos2))
