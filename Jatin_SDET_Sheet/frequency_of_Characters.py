'''
Program to find the frequency of each character in a string

ip: "hello world"
op: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

Explanation: The frequency of each character in the string "hello world" is as follows:

'''
class Frequency: 
    def __init__(self,str): 
        self.str = str 

    def frequencyOfCharacters(self): 
        characterString = self.str 
        seen={} 
        for char in characterString: 
            if char in seen: 
                seen[char]+=1
            else: 
                seen[char]=1
        
        return seen

if __name__ == "__main__":
    str = input("Enter the string: ") 
    frequencyOfCharacters = Frequency(str) 

    print(f"Frequency of each character in the {str} is: ", frequencyOfCharacters.frequencyOfCharacters()  )

