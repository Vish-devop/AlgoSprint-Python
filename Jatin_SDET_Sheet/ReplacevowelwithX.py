# replace all the vowels with "x" in the given string 

class ReplaceVowelWithX:
    def __init__(self,str): 
        self.str=str

    def replaceVowelWithX(self): 
        vowels="aeiouAEIOU"
        string = list(self.str) 

        for i in range(len(string)): 
            if string[i] in vowels: 
                string[i] = "x"

        return "".join(string) 

if __name__=="__main__":
    string = input("Enter the string: ")
    replaceVowelwithX = ReplaceVowelWithX(string) 

    print(f"String after replacing all the vowels with 'x' in the original string: {string} is: ", replaceVowelwithX.replaceVowelWithX())