# # to find all unique palindrome in string
# # function To expand left and right pointers to find the longest palindrome
# def expand(s, left, right):
#     len_s = len(s)
#     while left >= 0 and right < len_s and s[left] == s[right]: ####
#         left -= 1
#         right += 1
#     return left+1, right-1


# # function to find all unique palindromes in string
# def get_unique_palindromes(s):
#     len_s = len(s)
#     result = set()  # using set, so that only unique palindromes will be returned
#     for i in range(len_s):
#         l1, r1 = expand(s, i, i)
#         l2, r2 = expand(s, i, i+1)

#         # condition to avoid single letters in odd palindrome case
#         if l1 != r1:
#             result.add(s[l1:r1+1])

#         # condition to check for even palindrome case
#         if l2 < r2:
#             result.add(s[l2:r2+1])

#         # returns set as a list so that no two are same
#     return list(result)


# # run this code if this file is executed directley in the terminal
# if __name__ == '__main__':
#     string = input("Enter a Word: ")
#     print(f"All unique palindromes are :{get_unique_palindromes(string)}")

def find_palindromes_in_sub_string(input, j, k, palindromeSet):
  while j >= 0 and k < len(input):
    if (input[j] != input[k]):
      break
    
    palindromeSet.add(input[j: k + 1]) #adding value in set, taking substring from j to k  

    j -= 1 #cabac 
    k += 1


def find_all_palindrome_substrings(input):
    
    palindromes = set()
    for i in range(0, len(input)):
        find_palindromes_in_sub_string(input, i - 1, i + 1,palindromes) # midlle elemnt  , no copy of odd element 
        find_palindromes_in_sub_string(input, i, i + 1,palindromes) #cabbac 

    print("Your required palindromes of length > 2 => ")
    count = 0
    for val in palindromes:
        if len(val)>2:
            print(val)
            count+=1
    return count


s = input("Enter the string to find the palindrome of => ")

print("Total palindrome substrings of length > 2 => ", find_all_palindrome_substrings(s))
