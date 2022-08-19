
def find_palindromes_in_sub_string(input, j, k):
  #count=0
  while j >= 0 and k < len(input):
    if input[j] != input[k]:
      break
    else:
        print(input[j: k + 1])
    #count += 1

    j -= 1
    k += 1

  return 


"""def find_all_palindrome_substrings(input):
  count = 0
  for i in range(0, len(input)):
    count += find_palindromes_in_sub_string(input, i - 1, i + 1)
    count += find_palindromes_in_sub_string(input, i, i + 1)"""

  #return count


s = "aabbbaa"
print("all palidrome",find_palindromes_in_sub_string(s,10,10))
#print("Total palindrome substrings: ", find_all_palindrome_substrings(s))