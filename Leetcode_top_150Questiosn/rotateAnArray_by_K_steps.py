'''
PS: Rotate an array (left) and (right) by k-steps. 
k could be any number (it's basically the index from where you need to rotate an array)

ip: [1,2,3,4,5]
k=3
op: 
(left rotation): [4,5,1,2,3]
(right rotation): [3,4,5,1,2]
'''

class Rotation:
    def __init__(self,arr,k):
        self.arr=arr
        self.k=k
        self.k%=len(array)
    
    def left_rotation(self): 
        '''
        In, left_rotation, the first(k) elements are moved to the end of an array. 
        My Approach: 
        - We would divide the array in 2-parts: 
            FirstPart: all the element before k
            SecondPart: all the elements after k
        - Then, we would concatenate both into a single array. 

        TC: O(n) + SC: O(n)
        '''
        array=self.arr
        
        firstArray=array[:self.k]
        secondArray=array[self.k:]
        leftRotation = secondArray + firstArray
        
        return leftRotation

    def right_rotation(self): 
        array=self.arr
        firstArray = array[-self.k:]
        secondArray=array[:-self.k]
        resultArray=firstArray+secondArray

        return resultArray
    
    # Follow-UP Question: Could you optimize it? (YES : Space Wise) 
    def rotationOptimized(self): 
        # rotating an array in-place..... 
        # TC: O(n) + SC: O(n) 
        array = self.arr 
        array.reverse() 

        # For left_rotation, reversing the elements before k and then reversing element post k. 
        array[:self.k]=reversed(array[:self.k])
        array[self.k:]=reversed(array[self.k:])

        return array 
    
    def leftRotation_without_slicing(self): 
        '''
        As many programming langugage, didn't have the feature of SLICING operator, therby tried to rotate and array without slicing oeprator. 
        (So, inspite of slicing operator we would be using modulur (%) operator) 
        TC: O(n) + SC: O(n) 
        '''
        array = self.arr 
        for _ in range(k): 
            first = array.pop(0) # removing the first element 
            array.append(first)  # appending it to end
        return array 
    
    def rightRotation_without_slicing(self): 
        array=self.arr
        for _ in range(k): 
            last = array.pop() 
            array.insert(0,last) 
        return array 

if __name__ == "__main__":
    array = [1,2,3,4,5]
    k=2
    rotateAnArray = Rotation(array,k) 

    print(f"Left rotated array", rotateAnArray.left_rotation())
    print("----------")
    print("Right rotated array by k steps: ",rotateAnArray.right_rotation())
    print("----------")
    print("Array rotation Optimized solution: ",rotateAnArray.rotationOptimized())

        
        
    
