'''
Problem statement: 
Given a string, print the even words from a string.
 
ip: This is a Coding Test
op: This a Test
Explanation: Indexes of "This", "a", "Test" are 0,2,4 which are even : that's why printing them. 
'''

class EvenWords: 
    def __init__(self,str):
        self.str=str
    
    def evenWordsFinder(self): 
        words= self.str.split() 
        print(words)

        evenWords=[]
        for word in words: 
            if words.index(word)%2==0: 
                evenWords.append(word)
        return " ".join(evenWords)
    
if __name__ == "__main__":
    str = input("Enter the string: ")
    evenWords=EvenWords(str) 

    print(f"Even words in the string: {str} are: ", evenWords.evenWordsFinder())

