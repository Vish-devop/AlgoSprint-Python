'''
Problem Statement: Reverse only letters in a string. 

ip: "Hello Python"
op: "Python Hello"
Explanation: The letters in the string "Hello Python" are reversed to form "Python Hello". 

'''

class ReverseOnlyLetters: 
    def __init__(self,str): 
        self.str = str 

    def reverseOnlyLetters(self): 
        string = self.str
        words = string.split()
        reversedWordsArray = words[::-1]

        return " ".join(reversedWordsArray)
    
    def reversingCharactersAndLetters(self): 
        string = self.str 
        words = string.split() 
        reversedArray = [] 

        for i in range(len(words)-1,-1,-1): 
            word  = words[i]
            reversedWord = word[::-1]
            reversedArray.append(reversedWord) 
        
        return " ".join(reversedArray) 
    
    def reverseOnlyCharacters(self): 
        string =self.str
        words = string.split() 

        reversedArray = []
        for word in words:
            reversedWord = word[::-1]
            reversedArray.append(reversedWord) 

        return " ".join(reversedArray)  
    
    def reversingWordsWithoutReversingSpecialCharacters(self): 
        '''
        In this, we're reversing the whole string but not the special characters. 
        eg: ip: Hello & Python
        op: Python & Hello

        In this qos, trying a new approach: 2Pointers
        '''
        string = self.str 
        words = string.split()

        left =0 
        right =len(words)-1
        specialChars = ['&','@','!','*','%','$','#','^','~']
        while left<right: 
            if words[left] in specialChars: 
                left+=1
            elif words[right] in specialChars: 
                right-=1
            else: 
                words[left],words[right]=words[right],words[left] 
                left+=1
                right-=1
            
        return " ".join(words) 


if __name__ == "__main__": 
    str = input("Enter the string: ") 
    reversedOnlyLetter = ReverseOnlyLetters(str)

    print(f"Reversed only letters in the string: {str} is: ", reversedOnlyLetter.reverseOnlyLetters())

    print("------------")

    print("Reversing both characters and letters in string: ", reversedOnlyLetter.reversingCharactersAndLetters())

    print("------------")

    print("Reversing only characters in string: ", reversedOnlyLetter.reverseOnlyCharacters())

    print("------------")
    print("Reversing words without reversing special characters in string: ", reversedOnlyLetter.reversingWordsWithoutReversingSpecialCharacters())





