# Print the second largest element in an array

class secondLargestElement: 
    def __init__(self,arr): 
        self.arr=arr

    def secondLargestElementFinder(self): 
        array = self.arr 
        firstLargest = secondLargest = 0

        for element in array: 
            if element>firstLargest: 
                secondLargest = firstLargest 
                firstLargest = element 
            
            elif element > secondLargest and element!=firstLargest: 
                secondLargest = element 
            
        return secondLargest 
        
if __name__ == "__main__": 
    array = [1,2,3,4,5]

    secondLargestElement = secondLargestElement(array) 
    print(f"Second largest element in the array: {array} is: ",secondLargestElement.secondLargestElementFinder())
