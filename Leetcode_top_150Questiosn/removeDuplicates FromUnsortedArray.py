'''
PS: Given an unsorted array, remove Duplicates from that array. 

ip: [1,2,2,4,5,3,2,3,1]
op: [4]
Explanation: Removed all the duplicates from that unsorted array. 
'''
class RemoveDuplicates: 
    def __init__(self,arr): 
        self.arr=arr
    
    def RemoveElementBruteForce(self): 
        '''
        ** very bad solution **
        1. Sorting the array. 
        2. Using 2-pointers removing the duplicates from an array
        3. returning the array. 
        
        TC: O(nlogn) + SC: O(1) 
        '''
        array = self.arr
        array.sort() 

        i=0
        for j in range(1,len(array)):
            if array[j]!=array[i]: 
                i+=1
                array[i]=array[j]
        
        return array[:i+1]
        # Problem is : this solution will fail where we have to preserve the order of elements. 
        


    def RemoveElement_Hashmap(self): 
        '''
        Using Hashmap (not an optimzed solution)
        1. Creating / storing the array elements into a hashmap (in key-value pairs) 
        2. if the value of any key is greater than 1, then just remove that element. 
        3. Return all the keys whole value == 1. 

        TC: O(n) + SC: O(n)
        '''
        seen={}
        for num in self.arr: 
            if num in seen: 
                seen[num]+=1
            else: 
                seen[num]=1
        result=[]
        for key,value in seen.items():
            if value==1: 
                result.append(key)
        return result
    
    def RemoveDuplicates_optmizedSolution(self): 
        '''
        This is the solution of Sorting + Two-Pointer approach, there we weren't able to preserve the order of elements.
        So, you can use HashSet() 

        TC: O(n) + SC: O(n)
        '''
        seen=set() 
        result = [] 

        for num in self.arr: 
            if num not in seen: 
                seen.add(num) 
                result.append(num) 
        return result  

    
if __name__ == "__main__":
    array = [1,2,2,5,4,3,2,3,1]
    removeDuplicates = RemoveDuplicates(array)

    print("Array without any duplicates: ", removeDuplicates.RemoveElement_Hashmap()) 

    print("----------------------")
    print("Array without duplicates: ", removeDuplicates.RemoveElementBruteForce())

    print("------------")
    print("Array without duplicates: ",removeDuplicates.RemoveDuplicates_optmizedSolution())
