def swapTwoNumbersUsingThirdVariable(number1, number2): 
    '''
    Swapping using 3rd variable. 
    '''
    print(f"Before swapping: number1 = {number1}, number2 = {number2}")
    temp=number1
    number2=number2
    number2=temp

    return number1,number2

def swapTwoNumbersWithoutThirdVariable(number1,number2):
    '''
    Swapping without using 3rd variable.
    '''
    print(f"Before swapping: number1 = {number1}, number2 = {number2}")

    number1=number1+number2
    number2=number1-number2
    number1=number1-number2

    return number1,number2

def swapTwoNumberUsingXOR(number1,number2):
    '''
    Swapping using XOR Operator
    '''
    print(f"Before swapping: number1 = {number1}, number2 = {number2}")
    numbwer1 = number1^number2
    number2=number1^number2
    number1=number1^number2

    return number1,number2

def swapTwoNumbersUsingPythonDefaultSwap(number1,number2):
    '''
    Swapping using python default swap
    '''
    print(f"Before swapping: number1 = {number1}, number2 = {number2}")
    number1,number2=number2,number1

    return number1,number2


if __name__ == "__main__":
    number1=10
    number2=20
    print("Using 3rd variable")
    number1,number2=swapTwoNumbersUsingThirdVariable(number1,number2)
    print(f"After swapping: number1 = {number1}, number2 = {number2}")
    print("Using without 3rd variable")
    number1,number2=swapTwoNumbersWithoutThirdVariable(number1,number2)
    print(f"After swapping: number1 = {number1}, number2 = {number2}")
    print("Using XOR")
    number1,number2=swapTwoNumberUsingXOR(number1,number2)
    print(f"After swapping: number1 = {number1}, number2 = {number2}")
    print("Using python default swap")
    number1,number2=swapTwoNumbersUsingPythonDefaultSwap(number1,number2)
    print(f"After swapping: number1 = {number1}, number2 = {number2}")
    print("Using python default swap")
    number1,number2=swapTwoNumbersUsingPythonDefaultSwap(number1,number2)
    print(f"After swapping: number1 = {number1}, number2 = {number2}")
    print("Using python default swap")
    number1,number2=swapTwoNumbersUsingPythonDefaultSwap(number1,number2)
    print(f"After swapping: number1 = {number1}, number2 = {number2}")
    