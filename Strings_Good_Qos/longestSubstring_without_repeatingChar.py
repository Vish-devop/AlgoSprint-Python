'''
Questions: 
Longest substring without repeating characters. 

Input: "abcabcbb"
Output: 3
Explanation:
The longest substring without repeating characters is "abc", which has a length of 3.
Other substrings like "bca" and "cab" also have length 3, but no substring without repeating characters is longer than 3.

'''
def longestSubstring_without_repeatingCharacters(string): 
    if len(string)==0: return "" 

    max_len=0
    substring=[]
    for i in range(len(string)): 
        seen=set()
        for j in range(i,len(string)): 
            if string[j] in seen: 
                break
            seen.add(string[j])
            curr_length=j-i+1

            if curr_length > max_len: 
                max_len = curr_length
                substring = [string[i:j+1]]
            elif curr_length==max_len: 
                substring.append(string[i:j+1])
    
    substring = list(set(substring))
    return substring, max_len
    
print(longestSubstring_without_repeatingCharacters("abcabcbb"))


def longest_substring_with_repeating_char(string): 
    max_len=0
    longest_substring = "" 
    for i in range(len(string)): 
        for j in range(i,len(string)):
            curr_len =j-i+1 
            substr=string[i:j+1]
            if len(set(substr))==1: 
                if len(substr)>len(longest_substring): 
                    longest_substring = substr
            
    return longest_substring 

print(longest_substring_with_repeating_char("abcabba")) 
