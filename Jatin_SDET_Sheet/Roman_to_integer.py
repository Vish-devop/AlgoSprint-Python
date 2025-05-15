'''
Problem Statement: 
Given a Roman Number, conver it it to an integer.

ip: "V"
op: 5

ip: "IV"
op: 4
'''

class RomanToInteger: 
    def __init__(self,roman): 
        self.roman = roman 

    def romanToInteger(self): 
        roman = self.roman
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total=0
        prev_value=0
        for char in roman[::-1]:
            current_value = roman_dict[char]
            if current_value < prev_value: 
                total-=current_value 
            else: 
                total+=current_value 
            prev_value = current_value 
        return total 
    
if __name__ == "__main__":
    roman = input("Enter the Roman Number: ")
    romanToInteger = RomanToInteger(roman) 

    print("Integer value of the Roman Number: ", roman, "is: ", romanToInteger.romanToInteger())
         

