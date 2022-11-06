#Write a function to find all duplicate elements of a list
def find_duplicate(lis):
    res=[]
    for i in range(0,len(lis)):
        for j in range(i+1,len(lis)):
            if lis[i] == lis[j]: 
             res.append(lis[i])
    return res         

#lis = [2, 33, 2, 33, 4]
lis = list(map(int,input("Enter array:").split()))
print("duplicate element are:",find_duplicate(lis))







