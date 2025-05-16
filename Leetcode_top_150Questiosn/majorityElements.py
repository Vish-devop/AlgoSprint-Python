'''
PS: Given an array, return the element whose frequency is maximum in the whole array. 

ip: [3,2,3]
op: 3 
Explanation: Because (3) is repeated 2 times and 2's frequency is only 1, that's why op is 3. 
'''

class MajorityElement: 
    def __init__(self, arr): 
        self.arr=arr

    def majorityElementUsingHashmap(self): 
        array=self.arr
        seen={} 
        for num in array: 
            if num not in seen: 
                seen[num]=1
            else: 
                seen[num]+=1
        
        maxValue, maxKey = 0,None
        for key,value in seen.items(): 
            if maxValue<value: 
                maxValue=value 
                maxKey=key 

        return maxKey 

    def majorityElement_boyeMoore(self): 
        '''
        Most optimized solution, using Booye-Moore Algorithm. 
        1. Initialize "Candidate = NONE" and count = 0.
        2. Traverse the array, 
            if count=0, set candidate = current_element
            if current_element == candidate, increemnt count 
            otherwise decrease the count. 
        3. Return candidate (as it's the majority element) 

        TC: O(n) + SC: O(1) 
        '''
        array = self.arr 
        candidate, count = None, 0 

        for num in array: 
            if count ==0: 
                candidate = num 
            count+=1 if num == candidate else -1
        
        count =0 
        for num in array: 
            if num == candidate: 
                count+=1 
        return candidate if count>len(array)//2 else None 


if __name__=="__main__":
    array = [3,2,3]
    majority_element= MajorityElement(array) 

    print(f"Majority element present in an array - {array} is: ",majority_element.majorityElementUsingHashmap())