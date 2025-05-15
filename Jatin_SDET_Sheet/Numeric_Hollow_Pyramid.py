'''
Problem Statement: 
Given a number n, print a hollow pyramid of numbers with n rows.

ip: 5

'''
class hollowPyramid: 
    def __init__(self,n): 
        self.n=n
    
    def hollowPyramidFinder(self): 
        n=self.n
        for i in range(n):
            for j in range(n-i-1): 
                print(" ", end= "") 
            for j in range(2*i+1): 
                if j==0 or j==2*i or i==n-1: 
                    print(i+1, end="")
                else: 
                            print(" ", end="")
                    print()
        return "" 

if __name__ == "__main__":
    n = int(input("Enter the number of rows for the hollow pyramid: "))

    hollowPyramid = hollowPyramid(n) 
    print("Hollow pyramid of numbers with n rows: ", n) 

    print(hollowPyramid.hollowPyramidFinder()) 
    