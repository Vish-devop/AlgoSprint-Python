'''
Valid Parenthesis : Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

ip: "({[]})"
op: True

'''
class ValidParenthesis: 
    def __init__(self,str): 
        self.str = str

    def isValid(self): 
        stack = [] 
        brackets = {
            '(': ')',
            '{': '}',
            '[': ']'
        }


        for char in self.str: 
            if char in brackets: 
                stack.append(char) 
            elif stack and char == brackets[stack[-1]]: 
                stack.pop() 
            else: 
                return False 
        return not stack 

if __name__ == "__main__":
    string = input("Enter the string: ") 
    validParenthesis = ValidParenthesis(string) 

    print(f"Is the string: {string} valid parenthesis: ", validParenthesis.isValid())
                    