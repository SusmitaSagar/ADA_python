#take input , unsorted list
#devide , middle element in right side
#merge by comparing
def mergesort(list1):
   if len(list1)>1:  
     mid = len(list1)//2  ##try num
     left_list=list1[:mid] #take all value from zero to before mid, doesnot include middle
     right_list=list1[mid:] #take all elemnet from middle till end
     mergesort(left_list)
     mergesort(right_list)
     i=0 #index of left list element , to access elemnt for comaprison
     j=0  # right side list element
     k=0 #of original list, for storing the merged list
     while i<len(left_list) and j<len(right_list):
          if left_list[i]<right_list[j]: #comparing elemnts
              list1[k]= left_list[i]
              i=i+1  #increace left pointer
              k=k+1 #increase index of newlist
          else:
            list1[k]=right_list[j]
            j=j+1
            k=k+1
     while len(left_list)>i:  #if after comparison , any elemnt is left , then we need to add that
        list1[k] = left_list[i] #cause if index is equal to len of list, ther loop will exit
        i=i+1
        k=k+1
     while len(right_list)>j: #for right list
        list1[k] = right_list[j]
        j=j+1
        k=k+1   

 #for takiing input from user    
num = int(input("enter the length of list:")) 
list1 = [int(input()) for x in range(num)]
mergesort(list1) #calling fn
print("sorted list is",list1)