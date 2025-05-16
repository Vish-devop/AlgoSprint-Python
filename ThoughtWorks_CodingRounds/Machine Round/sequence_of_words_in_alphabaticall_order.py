'''
Problem Statement: Displaying Words of a Sentence in Alphabetical Order

Given a sentence, arrange all words in alphabetical order while preserving their original case. Punctuation should be ignored during sorting, and words should be sorted case-insensitively.

Constraints:
- Words in the sentence are separated by spaces.
- Ignore punctuation and special symbols when sorting.
- Sorting should be case-insensitive, meaning "Apple" and "apple" are treated the same.
- If the sentence is empty or contains no words, return an empty result.

Example Scenarios:

Example 1
Input:
"The quick brown fox jumps over the lazy dog"
Output:
"brown dog fox jumps lazy over quick The the"
Explanation:
- Words are sorted alphabetically.
- "The" and "the" appear separately since sorting is case-sensitive for display but case-insensitive for logic.

Example 2
Input:
"Hello, world! Welcome to AI."
Output:
"AI Hello to Welcome world"
Explanation:
- Punctuation is ignored.
- Words are sorted alphabetically.

Example 3
Input:
"" (empty string)
OP: "" 
'''
class ReArrange_Words_Alphabatically: 
    def __init__(self,string): 
        self.string= string 

    def rearrange(self): 
        string = self.string 
        if not string: return " " 

        words = string.split(" ")
        #["Hello", "World", "Welcome", "To", "AI"]
        size=len(words) 
        for i in range(size): 
            for j in range(0,size-i-1): 
                if words[j].lower() > words[j+1].lower(): 
                    words[j], words[j+1] = words[j+1],words[j]
        
        return " ".join(words)

if __name__ == "__main__":
    string = "Hello World, Welcome to AI"
    sequenceOfWords = ReArrange_Words_Alphabatically(string) 

    print("new string: ", sequenceOfWords.rearrange())


