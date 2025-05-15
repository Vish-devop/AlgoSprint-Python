'''
(2) cases: 
First, move all zeros to right of the array. 

Second, move all zeros to left of the array. 

ip: [1,0,2,0,3,0,4,0]
op: (left-side): [0,0,0,0,1,2,3,4]
op: (right-side): [1,2,3,4,0,0,0,0]
Explanation:
The first case moves all zeros to the right side of the array, while the second case moves all zeros to the left side of the array.



'''
class MoveAllZeros: 
    def __init__(self,arr): 
        self.arr= arr 

    def moveAllZerosToRight(self): 
        array = self.arr 

        nonZeroCount = 0
        for i in range(len(array)): 
            if array[i]!=0: 
                array[nonZeroCount]=array[i]
                nonZeroCount+=1

        while nonZeroCount<len(array): 
            array[nonZeroCount]=0
            nonZeroCount+=1

        return array 

    def moveAllZerosToLeft(self):
        array=self.arr
        nonZeroCount=len(array) 
        for i in range(len(array)-1,-1,-1):
            if array[i]!=0: 
                array[nonZeroCount-1]=array[i]
                nonZeroCount-=1
        while nonZeroCount>0: 
            array[nonZeroCount-1]=0
            nonZeroCount-=1

        return array  

if __name__ == "__main__":
    array = [1,0,2,0,3,0,4,0]
    moveAllZeros = MoveAllZeros(array) 

    direction = input("Enter the direction of moving zeros (left/right): ").strip().lower() 

    if direction == "right":
        print(f"Array after moving all zeros to right: {moveAllZeros.moveAllZerosToRight()}")  
    else: 
        print(f"Array after moving all zeros to left: {moveAllZeros.moveAllZerosToLeft()}")