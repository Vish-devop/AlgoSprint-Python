'''
Question:  Longest Palindromic Substring: Write a function that takes a string and returns the longest palindromic substring within it.


Input: "babad"

Output: 3
A substring of the input string that is the longest palindrome.
For the above input, valid outputs are:
"bab" or "aba"
(Both are palindromic substrings of length 3.)

Explanation
A palindromic substring is a sequence of characters within the string that reads the same forwards and backwards.


'''
class longest_palindromic_substring: 
    def __init__(self, s): 
        self.s = s

    @staticmethod
    def check_palindrome(substring): 
        return substring == substring[::-1]

    def mainLogic(self):
        length = len(self.s) 
        maxLen = 0
        longest = ""
        for i in range(length): 
            for j in range(i, length): 
                substr = self.s[i:j+1]
                if self.check_palindrome(substr) and len(substr) > maxLen: 
                    maxLen = len(substr)
                    longest = substr
        return longest

if __name__ == "__main__":
    s = "babad"
    lps = longest_palindromic_substring(s) 
    print(lps.mainLogic())