#Write a function that returns
#all the permutation of the given string of length 
# https://www.youtube.com/watch?v=4lIQCoG4MnY&ab_channel=WrtTech
#we will use recursion here

def permuatations(word):
    if len(word)==1:
        return [word] #if length is 1,return the single word
   
    perms = permuatations(word[1:]) #return all except first word
    char = word[0]
    result = []

    for perm in perms:
       for i in range (len(perm)+1) :
        result.append(perm[:i]+char+perm[i:])

    return result

print(permuatations('abc'))        
 
