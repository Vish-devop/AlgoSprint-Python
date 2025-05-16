'''
Problem Statment: 
Given two sorted arrays, merge them into a single sorted array.

ip: [1,3,5,7], [2,4,6,8]
op: [1,2,3,4,5,6,7,8]
Explanation: The merged array is [1,2,3,4,5,6,7,8] which is sorted in ascending order.
'''

class MergeSortedArrays: 
    def __init__(self,arr1,arr2): 
        self.arr1=arr1
        self.arr2=arr2

    def mergeSortedArraysUsingExtraMemory(self):
        ''' TC: O(n) + SC: O(n) ''' 
        mergedArrays=[]

        i,j=0,0
        while i<len(self.arr1) and j<len(self.arr2): 
            if self.arr1[i]<self.arr2[j]: 
                mergedArrays.append(self.arr1[i])
                i+=1
            else: 
                mergedArrays.append(self.arr2[j])
                j+=1
        
        while i<len(self.arr1): 
            mergedArrays.append(self.arr1[i])
            i+=1
        
        while j<len(self.arr2): 
            mergedArrays.append(self.arr2[j])
            j+=1
        

        return mergedArrays

    def mergeSortedArraysWithoutExtraMemeory(self): 
        ''' TC: O(nlogn) + SC: O(1) '''
        mergedSortedArrays = self.arr1+self.arr2
        mergedSortedArrays.sort() 

        return mergedSortedArrays
    

if __name__ == "__main__":
    arr1=[1,2,4,5]
    arr2=[3,4,5,6]

    mergedSortedArrays = MergeSortedArrays(arr1,arr2)

    print(f"Merged sorted arrays using extra memory: {mergedSortedArrays.mergeSortedArraysUsingExtraMemory()}")

    print("-------")

    print(f"Merged sorted arrays without extra memory: {mergedSortedArrays.mergeSortedArraysWithoutExtraMemeory()}")




