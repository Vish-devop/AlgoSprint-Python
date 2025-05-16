'''
Problem Statement: Remove Duplicates from Sorted Arrays 

ip: [1,1,2]
op: 2
Explanation: The array is sorted and contains duplicates. The function should return the length of the array after removing duplicates.
Return_Type: Array 
''' 
class RemoveDuplicatesFromSortedArray: 
    def __init__(self,arr): 
        self.arr=arr
        self.length=len(arr) 

    def removeDuplicates(self): 
        '''
        1. We would traverse through the array and check if the current element is equal to the next element; 
        if true -> then we would swap the current element with the last element of the array.
        2. We would also keep track of the last index of the array, so that we can return the length of the array after removing duplicates. 
        
        TC: O(n) + SC: O(1) { Because not taking help of new memory }
        '''
        array = self.arr
        if not array: return []
        array_size = self.length 

        i=0 
        for j in range(1,array_size):
            if array[j]!=array[i]:
                i+=1
                array[i]=array[j]
        
        return array[:i+1]

    def removeElementUsingHashmap(self):
        '''
        Removing elements using hashmap. 
        1. Creating / storing the array_elements into hashmap. 
        2. Returning only those keys whole value = 1.

        TC: O(n) + SC: O(n)
        '''
        seen={}
        for char in self.arr:
            if char not in seen: 
                seen[char]+=1
            else: 
                seen[char]=1
        
        result=[]
        
        for key,value in seen.items():
            if value==1: 
                result.append(key)
        
        return result

if __name__=="__main__":
    array = [1,2,2,3]
    removeDuplicates = RemoveDuplicatesFromSortedArray(array)

    print("New array post removing the duplicates from the array: ",removeDuplicates.removeDuplicates())
    print("----------------------")
    print("New array post removing duplicates from sorted arrays, ", removeDuplicates.removeDuplicates())

                


