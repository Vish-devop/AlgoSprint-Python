'''
Problem Statement: Removing Specific Characters from a String

Given a string and a set of specific characters, remove all occurrences of those characters from the string while preserving the order of the remaining characters. The removal should be case-sensitive, meaning uppercase and lowercase letters are treated as different characters.
Constraints:
- The input string may contain letters, digits, spaces, or special characters.
- The set of characters to remove will be provided separately.
- If the input string is empty, return an empty result.
- If no characters match those to be removed, return the original string unchanged.
Example Scenarios:

Example 1
Input:
- String: "hello world!"
- Characters to remove: "lo"
Output:
"he wrd!"
Explanation:
- The characters 'l' and 'o' are removed from "hello world!", leaving "he wrd!".

Example 2
Input:
- String: "AABaaBB"
- Characters to remove: "AB"
Output:
"aa"

Explanation:
- 'A' and 'B' are removed, case-sensitive—so 'a' remains.
Example 3
Input:
- String: "abc@123"
- Characters to remove: "@1"
Output:
"abc23"

Explanation:
- '@' and '1' are removed, leaving "abc23".


'''

class RemoveChars: 
    def __init__(self,string,remove_str): 
        self.string=string
        self.remove_str=remove_str

    def removecharacter(self): 
        '''
        Brute-Force Method
        TC: O(n) + SC: O(n) 
        '''
        result = ""
        str=self.string
        for char in str: 
            if char not in self.remove_str: 
                result+=char
            else: 
                continue
        return result 
    
    def removeCharsWithout_extra_space(self): 
        # in-place modification 
        # TC: O(n) + SC: O(1)
        char_list = list(self.string) 
        idx =0

        for char in char_list: 
            if char not in self.remove_str: 
                char_list[idx]=char
                idx+=1
        
        return "".join(char_list[:idx])


if __name__ == "__main__":
    string = input("Enter the string: ")
    removeChars=input("Enter the char/string: ")

    removeSpecifiedChars = RemoveChars(string,removeChars)

    print("new string: ",removeSpecifiedChars.removecharacter())

    print("--------------------")

    print("new string: ",removeSpecifiedChars.removeCharsWithout_extra_space())