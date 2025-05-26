'''
Problem Statement:
Design a class Book with the following:

Attributes: title, author, price

Method: display_details() → prints all book details

Expected Output Example:

python
Copy code
Book: Atomic Habits
Author: James Clear
Price: 499
'''

class Book: 
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price 

    def display_details(self): 
        return f"Details of your book are: Title- {self.title}, Author- {self.author}, Price- {self.price}"

if __name__=="__main__":
    obj = Book("Atomic Habits", "James Clear", 499)

    print(obj.display_details())
        