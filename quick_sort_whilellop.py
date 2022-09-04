#to get the correct position of the pivot elemen

def pivot_place(list1,first, last): #starting and last_index
    pivot = list1[last]
    left = first
    right = last-1
    #we have stooping condition, comapring index and pivot value
    while True:
        while left<=right and list1[left] <= pivot: # if both condition is true, we need not to do anything
          left = left+1 #just increment the left
         #if above condition is false, compare at other end value
        while left<=right and list1[right]>= pivot:
           right=right-1
        if right<left:
            break
            #list1[first], list1[right] = list1[right] , list1[first] #making changes in list
           
        else:
             list1[left],list1[right] = list1[right],list1[left]
    list1[last], list1[left] = list1[left] , list1[last] 
    #pivot  ,right_index_value =  
    return left    # for position of pivot element

def quicksort(list1,first,last):
    if first<last:
       p=pivot_place(list1,first,last)
       quicksort(list1,first,p-1) #recursively sorting 
       quicksort(list1,p+1,last) #recursively sorting 

#main
"""list1=[56,73,34,65,33,22,1] 
n = len(list1)
quicksort(list1,0,n-1)  
print(list1)  """ 
#for taking input from user
n = int(input("enter the length of list:")) 
list1 = [int(input()) for x in range(n)]
quicksort(list1,0,n-1)
print("sorted list is",list1)





