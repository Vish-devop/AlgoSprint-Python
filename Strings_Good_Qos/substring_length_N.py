'''
Qos: Substrings of Length N: Create a function that generates all substrings of a given length n from a string. Then, return how many of those substrings are palindromes.

Input: "ababa", n = 3
Output: 3
Explanation: The substrings of length 3 are: "aba", "bab", "aba". All three are palindromes, so the function returns 3.

'''
def check_palindrome(string): 
    return string==string[::-1]

def substrings(string,n):
    # result=[]
    count=0
    for i in range(len(string)): 
        for j in range(i,len(string)): 
            substring=string[i:j+1]
            if check_palindrome(substring) and len(substring)==n: 
                count+=1
    return count 

print(substrings("ababa",3))
    