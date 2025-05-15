class reverseAnInteger: 

    def __init__(self,number):
        self.number=number

    def reverseInStandardWay(self):
        reversedNumber=0
        newNumber = self.number
        
        while (newNumber!=0):
            digit = newNumber%10
            reversedNumber = reversedNumber*10 + digit
            newNumber = newNumber//10

        return reversedNumber
    
    def reverseInStringWay(self):
        '''
        First, converting the integer into string, thereby reversing the string and then converting it back to integer. 
        '''
        stringNumber = str(self.number)
        reversedNumber = stringNumber[::-1]
        return int(reversedNumber) 

if __name__ == "__main__":
    number = int(input("Enter the number to be reversed: "))
    
    reversedInteger = reverseAnInteger(number) 
    
    print(f"Reversed in standard way: {reversedInteger.reverseInStandardWay()}")

    print("-------------------")

    print(f"Reversed in string way: {reversedInteger.reverseInStringWay()}")



    