#making a function for binary search in recursion
def search(arr,low,high,key):
    if high>=low:
        mid=(high+low)//2  #the floor division // rounds the result down to the nearest whole number
    if arr[mid]==key:   #the mid elemnt is the  key
        return mid  
    elif arr[mid]>key: #if key is less than mid elemnt(compare)
        return search(arr,low,mid-1,key) # call thr recursion fn
    elif arr[mid]>key:
        return search(arr,mid+1,high,key)   #key is greater than mid elemnt
    else:
        return ("element is not present")    
ar=[1,2,5,6,8,9]
print("my arr is",ar)
#tar=8
tar=int(input("enter target value"))
print(search(ar,1,9,tar))
