'''
Even Length Palindrome Check: Write a function that checks if the middle two characters of a string (if the string has even length) are the same. If so, return true; otherwise, return false.

Input and Output Examples
Example 1
Input: "abccba"
Step 1: The string length is 6 (even).
Step 2: The middle two characters are at positions 2 and 3 (0-based indexing):
s[2] = 'c'
s[3] = 'c'
Step 3: Both are 'c', so they are the same.
Output: True
'''

class Even_length_palin: 
    def __init__(self,s):
        self.s=s
    
    def mainLogic(self): 
        #edge case: if length of string is odd, return False. 
        if len(self.s)%2 !=0: 
            return False 
        
        mid1=len(self.s)//2-1
        mid2=len(self.s)//2 

        return self.s[mid1]==self.s[mid2]

if __name__ == "__main__":
    s="abccba"
    evenLength = Even_length_palin(s)

    print(evenLength.mainLogic())
    