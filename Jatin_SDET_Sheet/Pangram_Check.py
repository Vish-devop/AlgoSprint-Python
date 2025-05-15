'''
Problem Statement: 
Given a string, check if it is a pangram or not.

ip: "The quick brown fox jumps over the lazy dog"
op: True
Explanation: The string contains all the letters of the alphabet, so it is a pangram.

'''
class PangramCheck: 
    def __init__(self,str): 
        self.str=str
    
    def isPangram(self): 
        string = self.str
        alphabet = set("abcdefghijklmnopqrstuvwxyz")

        stringSet = set(string.lower())

        return alphabet.issubset(stringSet) 
    
if __name__ == "__main__":
    string = input("Enter the string: ")

    pangramCheck = PangramCheck(string) 

    print(f"Is the string: {string} a pangram? ", pangramCheck.isPangram())