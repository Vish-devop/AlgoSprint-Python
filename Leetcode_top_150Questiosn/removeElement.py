'''
Problem Statement: 
Remove an element from an array and return the length of the array, post removal. 

ip: [3,2,2,3], val = 3
op: 2
Explanation: After removing the element 3, the array becomes [2,2], and its length is 2.

Constraints: Do not create a new array. 

'''
class RemoveElement: 
    def __init__(self,arr,val): 
        self.arr=arr
        self.val=val
    
    def removeElementUsingextraSpace(self): 
        '''
        1. Creating a new array that would store all the element except hte value. 
        2. Traverse through the original array and parallely check if the current element doesn't equal to the value; if true-> then append same element into new array, otherwise continue with traversal. 
        3. return the length of new array. 

        TC: O(n) + SC: O(n)
        '''
        newArray=[]
        for num in self.arr: 
            if num!=self.val: 
                newArray.append(num) 
        return len(newArray) 
    
    def removeElementWithoutExtraSpace(self): 
        '''
        More optimized solution, as TC: O(n) + SC: O(1) 
        1. We would traverse through the original array and check if the current element is equal to the value; 
        if true -> then we would swap the current element with the last element of the array. 
        '''
        lastIndex = len(self.arr)-1 
        for i in range(len(self.arr)):
            if self.arr[i] == self.val: 
                self.arr[i], self.arr[lastIndex] = self.arr[lastIndex], self.arr[i]
                lastIndex -=1
        return lastIndex+1
    

if __name__=="__main__":
    array=[3,2,3]
    val = 3

    removeElement = RemoveElement(array,val) 
    print(f"Length of the array after removing the element {val} from the array {array} is: ", RemoveElement(array,val).removeElementUsingextraSpace())

    print("--------")

    print(f"Length of the array after removing the element {val} from the array {array} is: ", removeElement.removeElementWithoutExtraSpace())