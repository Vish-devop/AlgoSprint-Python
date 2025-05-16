'''
Problem 1: Test Action Validator (Medium, 25 minutes, Array/String)
Description: You’re building an automation tool to validate a sequence of test actions for a UI testing framework. The actions are given as a string containing characters: 'C' (click), 'I' (input), 'V' (verify). A sequence is valid if:

Every 'I' is immediately followed by a 'V'.
'C' cannot be the last action.
At least one 'V' exists in the sequence. Write a function that takes a string of actions and returns True if the sequence is valid, False otherwise.

-----
Input: "CIV"
Output: True
Input: "CIC"
Output: False  # 'C' is last
Input: "IVC"
Output: True
Input: "CI"
Output: False  # 'I' not followed by 'V', no 'V' present
'''

def Test_Action_Validator(string): 
    # Case(1): Atleast 1 'V' must exist in the sequence. 
    if not string or "V" not in string: 
        return False 
    
    #Case(2): "C" should not present at last of the string. 
    if string[-1]=="C": 
        return False 

    #Case(3): "V" must not be followed by "I".
    for i in range(len(string)-1): 
        if string[i]=="I" and string[i+1]!="V": return False 
    
    return True 

print(Test_Action_Validator("CIC"))