'''
Problem Statement: Count Character Occurrences in a String

You are given a string consisting of alphanumeric characters, symbols, or spaces. Your task is to determine how many times each character appears in the string and return the result in a structured format.
Constraints:
- The string can contain uppercase and lowercase letters, digits, special characters, and spaces.
- The character count should be case-sensitive (i.e., 'A' and 'a' are considered different characters).
- The output should present characters sorted by their order of first appearance in the string.
- If the input string is empty, return an empty result.
Input & Output Examples
Example 1
Input: "hello world"
Output:
h: 1  
e: 1  
l: 3  
o: 2  
(space): 1  
w: 1  
r: 1  
d: 1  


Explanation:
- The character 'h' appears once.
- The character 'e' appears once.
- The character 'l' appears three times.
- The character 'o' appears twice.
- A space (' ') appears once.
- The rest appear once each.
Example 2
Input: "AABaaBB"
Output:
A: 2  
B: 2  
a: 2  
B: 1  


Explanation:
- Case-sensitive counting ensures 'A' and 'a' are treated separately.
- 'A' appears twice, 'B' appears three times, 'a' appears twice.
Example 3
Input: "" (empty string)
Output:
(empty result)


Explanation:
- Since the input string is empty, there are no characters to count.



'''
class Count_character_in_string: 
    def __init__(self,str): 
        self.str= str 

    def countCharacters(self): 
        string = self.str
        seen={} 
        for char in string: 
            if char not in seen: 
                seen[char]=1
            else: 
                seen[char]+=1
    
        return seen
     
 
if __name__=="__main__":
    string = input("Enter the string: ")
    countCharacters = Count_character_in_string(string) 

    print("------------")
    print(countCharacters.countCharacters())