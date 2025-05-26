'''
Question: 
Mirror Palindrome: Check if a string reads the same backward and forward using only alphanumeric characters and ignoring cases. Return true if it is a "mirror palindrome".

Input: "A man, a plan, a canal: Panama"
Output: True
Explanation:
First, remove all non-alphanumeric characters and ignore case, so the string becomes "amanaplanacanalpanama".
Now, check if this cleaned string reads the same forward and backward.
Since "amanaplanacanalpanama" is the same when reversed, the function returns True.
A "mirror palindrome" ignores spaces, punctuation, and case, focusing only on the sequence of letters and digits.

'''

def checkPalindrome(string): 
    return string == string[::-1]

def mirror_palin(string): 
    string=string.lower()
    result="" 
    for i in string: 
        if i.isalnum(): 
            result+=i
    
    if checkPalindrome(result):
        return True 
    return False 

print(mirror_palin("A man, a plan, a canal: Panama"))