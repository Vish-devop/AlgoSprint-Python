'''
Question: Adjacent Palindrome Check: Write a function that checks if a string can be split into two parts such that both parts are palindromes.

Input: "noonmadam"
Output: True
Explanation: The string can be split as "noon" and "madam", both of which are palindromes. So, the function returns True.

Input: "racecar"
Output: True
Explanation: 
Possible splits:
"r" | "acecar"
"ra" | "cecar"
"rac" | "ecar"
"race" | "car"
"racec" | "ar"
"raceca" | "r"

'''

def checkPalindrome(string): 
    return string==string[::-1]

def adjacent_palin(s): 
    for i in range(len(s)): 
        firstHalf=s[0:i]
        secondHalf=s[i:len(s)]

        if checkPalindrome(firstHalf) and checkPalindrome(secondHalf): 
            return True 
    return False 

print(adjacent_palin("noonmadam"))
        

