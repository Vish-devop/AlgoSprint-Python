'''
Problem Statement: 
Given a string, print the unique characters from the string. 

ip: "hello world"
op: "helo wrd"
Explanation: The unique characters in the string "hello world" are 'h', 'e', 'l', 'o', ' ', 'w', 'r', and 'd'.

'''

class UniqueCharacters: 
    def __init__(self,str): 
        self.str= str 

    def uniqueCharacters(self): 
        string = self.str 
        seen = {} 
        for char in string: 
            if char not in seen: 
                seen[char]=1
            else:
                seen[char]=1
        
        uniqueChars=""
        for char in seen: 
            uniqueChars+=char
        return uniqueChars

if __name__ == "__main__":
    string = input("Enter the string: ")
    uniqueChars= UniqueCharacters(string)

    print(f"Unique Characters in the string: {string} are: ", uniqueChars.uniqueCharacters())
