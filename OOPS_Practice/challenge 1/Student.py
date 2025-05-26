'''
Problem Statement:
Create a class Student with:
Attributes: name, roll_no, marks (out of 100)
Method: is_passed() → returns True if marks >= 40

Bonus: Add display_info() method.

'''
class Student: 
    def __init__(self,name,roll_no,marks): 
        self.name=name
        self.roll_no=roll_no
        self.marks=marks 

    def is_passed(self): 
        if self.marks>=40: 
            return True 
        
    def display_info(self): 
        print(f"Name: {self.name}")
        print(f"Roll No. : {self.roll_no}")
        print(f"Marks: {self.marks}")
        print(f"Status: {'Passed' if self.is_passed() else 'Failed'}")
        
if __name__=="__main__":
    student = Student("James",1,50)

    student.display_info()