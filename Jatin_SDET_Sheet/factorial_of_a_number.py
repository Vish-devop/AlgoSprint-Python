class Factorial: 
    def __init__(self,number): 
        self.number = number

    def factorialInStandardWay(self): 
        fact = 1
        while (self.number>0):
            fact = fact*(self.number)
            self.number-=1
        
        return fact 
    
if __name__ == "__main__":
    number = int(input("Enter the number whoe factorial you want to find: "))
    fact = Factorial(number)

    print(f"Factorial of the number: {number} is: ", fact.factorialInStandardWay())

