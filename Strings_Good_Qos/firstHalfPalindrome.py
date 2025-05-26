'''
Question: 
First Half Palindrome: Given a string, return true if the first half of the string is a palindrome. If the string has an odd length, ignore the middle character.

Example: 
Input: "abccba"
First half: "abc"
Is "abc" a palindrome?
Reverse: "cba"
Not the same as "abc"
Output: False


'''

class first_half_palindrome: 
    def __init__(self,s):
        self.s=s
    
    @staticmethod
    def checkPalindrome(substring):
        return substring==substring[::-1]
    
    def main_logic(self): 
        middleElement  = len(self.s)//2 
        firstHalf_string = self.s[0:middleElement]
        return self.checkPalindrome(firstHalf_string)

if __name__=="__main__":
    str="abccba"
    palindrome = first_half_palindrome(str) 

    print(palindrome.main_logic())

