'''
Question is to Return True if after removing the first and last character of the string, the string is palindrome in nature. 
'''



def is_palindrome(s): 
    return s==s[::-1]

def main_logic(s): 
    i,j=0,len(s)
    while j-i >2: 
        current_substring = s[i:j+1]
        if is_palindrome(current_substring): 
            return True 
        i+=1
        j-=1

s="abbcd"
print(is_palindrome(s))
