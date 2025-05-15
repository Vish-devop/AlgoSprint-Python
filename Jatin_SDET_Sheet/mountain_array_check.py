'''
Problem Statement: Mountain Array Check 
Given an array of integers, check if it is a mountain array or not.
A mountain array is an array that first increases to a peak and then decreases.

ip: [1, 2, 3, 4, 5, 4, 3, 2, 1]
op: True
Explanation: The array first increases to the peak (5) and then decreases, so it is a mountain array.

peak is the highest point in the array, and it is not equal to the first or last element.

Approach:
1. Check if the array has at least 3 elements (minimum required for a mountain array).
2. Traverse the array to find the peak:
    - The peak is the highest point where the array stops increasing and starts decreasing.
3. Ensure the peak is not the first or last element.
4. Verify the array strictly increases before the peak and strictly decreases after the peak.
5. If all conditions are satisfied, return True; otherwise, return False.

'''

class MountainArrayCheck: 
    def __init__(self,arr): 
        self.arr = arr 
    
    def isMountainArray(self): 
        array = self.arr 
        size = len(array) 

        if size<3: 
            return False 
        
        peak =0 
        for i in range(1,size): 
            if array[i]>array[i-1]: 
                peak=i
            else: 
                break
        
        print(array[peak])
        
        if peak ==0 or peak ==size-1: 
            return False 
        
        for i in range(peak+1,size): 
            if array[i]>=array[i-1]:
                return False 
        return True 

if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    mountainArrayCheck = MountainArrayCheck(array) 

    print(f"Is the array {array} a mountain array? ", mountainArrayCheck.isMountainArray())