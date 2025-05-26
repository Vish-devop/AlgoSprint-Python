'''
Question: Anagram of Palindrome: Write a function to check if a given string can be rearranged into a palindrome (i.e., if any of its permutations is a palindrome).

Input: "carrace"
Output: True
Explanation: The string "carrace" can be rearranged to form "racecar", which is a palindrome. A string can be rearranged into a palindrome if at most one character has an odd count (for odd-length strings), or all characters have even counts (for even-length strings). In "carrace", all characters except one ('e') have even counts, so it can be rearranged into a palindrome.

'''
def anagram_palindrome(string): 
    freq={} 
    for char in string: 
        if char not in freq:
            freq[char]=1
        else: 
            freq[char]+=1
    
    odd_count=0
    for key in freq: 
        if freq[key]%2!=0: 
            odd_count+=1
    
    if odd_count>1: 
        return False 
    return True 

print(anagram_palindrome("carrace"))