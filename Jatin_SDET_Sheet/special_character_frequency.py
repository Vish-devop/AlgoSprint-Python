'''
Given a string containing special characters, find the frequency of each special character in the string.

ip: "hello@world!@2023"
op: {'@': 2, '!': 1}
Explanation: The frequency of each special character in the string "hello@world!@2023" is as follows:

'''
class SpecialCharacterFrequency: 
    def __init__(self,str): 
        self.str= str

    def frequencyOfSpecialCharacters(self): 
        specialCharacterFrequency = self.str 
        specialChars = ['@','!','*','%','$','#','^','~']

        seen = {} 
        for char in specialCharacterFrequency: 
            if char in specialChars: 
                if char in seen: 
                    seen[char]+=1
                else: 
                    seen[char]=1
        return seen 
    
if __name__ == "__main__":
    string = input("Enter the string: ")
    specialCharacterFrequency = SpecialCharacterFrequency(string) 

    print("Frequency of each special character in the string: ",string, "is: ", specialCharacterFrequency.frequencyOfSpecialCharacters())

    