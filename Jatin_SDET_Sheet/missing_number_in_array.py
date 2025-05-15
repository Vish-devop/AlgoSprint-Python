'''
Problem statement: 
Given an array of n integers, find the missing number in the array.

ip: [1,2,3,4,5,6,7,8,9,10]
op: 11
Explanation: The array is missing the number 11.

'''

class MissingNumber: 
    def __init__(self,arr): 
        self.arr=arr
    
    def missingNumberFinder(self): 
        missingNumber = 0
        for i in range(1,len(self.arr)+1): 
            if i not in self.arr: 
                missingNumber = i 
                break 
        
        return missingNumber
    
if __name__ == "__main__":
    array = [1,2,3,4,5,6,7,81,10]
    missingNumber = MissingNumber(array)

    print(f"Missing number in the array: {array} is: ", missingNumber.missingNumberFinder())
    print("-------------------")