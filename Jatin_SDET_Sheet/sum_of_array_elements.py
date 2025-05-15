'''
Problem Statement:
Given an array of n integers, find the sum of all the elements in the array.

ip: [1,2,3,4,5]
op: 15
Explanation: The sum of all the elements in the array is 1+2+3+4+5 = 15.

'''
class SumOfArrayElements: 
    def __init__(self,arr): 
        self.arr=arr

    def sumOfArrayElements(self): 
        array=self.arr

        sum =0 
        for element in array: 
            sum+=element 
        return sum 

if __name__ == "__main__":
    array = [1,2,3,4,5]
    sumOfArrayElements = SumOfArrayElements(array)

    print(f"Sum of all the elements in the array: {array} is: ", sumOfArrayElements.sumOfArrayElements())
