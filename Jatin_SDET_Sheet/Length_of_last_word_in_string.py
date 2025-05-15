class Last_word_length:

    def __init__(self,str):
        self.str = str

    def lengthOfLastWord(self): 
        words = self.str.split() # ["Hello", "World"]
        lastword=words[-1]

        return len(lastword)
    
if __name__ == "__main__":
    str = input("Enter the string: ")

    lastWord = Last_word_length(str)

    print(f"Length of last word in the string: {str} is: ", lastWord.lengthOfLastWord())



