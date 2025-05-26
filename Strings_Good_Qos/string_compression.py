'''
String Compression: Implement a function that compresses a given string by converting sequences of the same character into their counts 

input: aaabb
output: a3b2
'''

def stringn_compression(string): 
    result=[]
    count=1
    for i in range(len(string)): 
        if string[i]==string[i-1]:
            count+=1
        else: 
            result.append(string[i-1]+str(count))
            count=1
        
    result.append(string[-1]+str(count))
    return ''.join(result) 
print(stringn_compression("aabbaa"))

# def string_compression(string): 
#     if not string: return "" 
#     result = "" 
#     seen={}
#     for char in string: 
#         if char not in seen: 
#             seen[char]=1
#         else: 
#             seen[char]+=1
    
#     for key,values in seen.items(): 
#         result+=f"{key}{values}"
#     return result 

# print(string_compression("aaabbaa")) 