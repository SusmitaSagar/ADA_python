#making a function for binary search in recursion
def search(arr,low,high,key):
    if high>=low:
        mid=(high+low)//2  #the floor division // rounds the result down to the nearest whole number
    if arr[mid]==key:   #the mid elemnt is the  key
        return mid  
    elif arr[mid]>key: #if key is less than mid elemnt(compare)
        return search(arr,low,mid-1,key) # call thr recursion fn
    else:
        return search(arr,mid+1,high,key)   #key is greater than mid elemnt
ar=[1,2,5,6,8,9]
tar=8
print(search(ar,1,9,tar))
