#to get the correct position of the pivot elemen

def pivot_place(list1,first, last): #starting and last_index
    pivot = list1[last]
    ptr = first #last element is pivot, first eleemnt is pointer
    #we have stooping condition, comapring index and pivot value
    for i in range(first,last):
        if list1[i] <= pivot:
            list1[i],list1[ptr] = list1[ptr],list1[i]
            ptr += 1

    list1[ptr], list1[last] = list1[last],  list1[ptr]
    return ptr      


def quicksort(list1,first,last):
    if len(list1) ==1:
        return list1

    if first<last:
       p=pivot_place(list1,first,last)
       quicksort(list1,first,p-1) #recursively sorting left
       quicksort(list1,p+1,last) #recursively sorting 
    return list1   

#main
list1=[56,73,34,65,33,22,1] 
n = len(list1)
quicksort(list1,0,n-1)  
print(list1)   
#for taking input from user
n = int(input("enter the length of list:")) 
list1 = [int(input()) for x in range(n)]
quicksort(list1,0,n-1)
print("sorted list is",list1)





