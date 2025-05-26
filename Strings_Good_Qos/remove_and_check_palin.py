'''
Quesetion: 
Remove and Check Palindrome: Given a string, repeatedly remove the first and last character until the string is less than 4 characters. Return true if any of those substrings is a palindrome.

Input: "abccba"
Output: True
Explanation:

Start with "abccba" (length 6, check if palindrome: yes, so return True).
If not, remove first and last: "bccb" (length 4, check if palindrome: yes, so return True).
If not, remove again: "cc" (length 2, less than 4, stop).
Since at least one substring ("abccba" or "bccb") is a palindrome, the function returns True.
'''

def check_palindrome(string): 
    return string==string[::-1]

def remove_and_check(string): 
    i=0
    j=len(string) 
    
    while (j-i)>=4: 
        substr=string[i:j+1]
        if check_palindrome(substr): 
            return True 
        i+=1
        j-=1
    return False 

print(remove_and_check("abcdef"))

