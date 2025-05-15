class reverseVowels: 
    def __init__(self,str): 
        self.str=str 

    def reversedVowels(self): 
        vowels="aeiouAEIOU"

        string = list(self.str)
        print(string) 
        left = 0
        right = len(string)-1

        while left<right: 
            if string[left] not in vowels: 
                left+=1
            elif string[right] not in vowels: 
                right-=1
            else: 
                string[left],string[right]=string[right],string[left]
                left+=1
                right-=1
        return ''.join(string)
    
if __name__ == "__main__": 
    str = input("Enter the string: ")
    reversedVowel = reverseVowels(str) 

    print(f"Reversed Vowels in the original string: {str} is: ", reversedVowel.reversedVowels())