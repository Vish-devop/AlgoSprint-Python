'''
Question: 
 Count Palindromic Subsequences: Write a function that counts the number of palindromic subsequences in a given string.

Input: "abcb"
Output: 6
Explanation: The palindromic subsequences are: "a", "b", "c", "b", "bcb", and "aba" (each single character is a palindrome, and "bcb" and "aba" are palindromic subsequences formed by skipping some characters). The function should count all such subsequences.
'''

def check_palindrome(string): 
    return string==string[::-1]

def count_palindromes(string): 
    count=0
    longest=[]
    for i in range(len(string)): 
        for j in range(i,len(string)): 
            substr=string[i:j+1]
            if check_palindrome(substr): 
                count+=1
                longest.append(substr)
    return count,longest 

print(count_palindromes("aaa"))