import datetime
import os

# os.getcwd()

class LMS: 
    """
    It has total 4 modules:
    1. display book
    2.issue book
    3. return books
    4. add books
    """

    # constructor

    def __init__(self, list_of_books, library_name):
        self.list_of_books = "List_of_books.csv"
        self.library_name = library_name
        self.books_dict = {}
        Id = 101
        with open(self.list_of_books) as bk:
            content = bk.readlines()
        for line in content: 
            self.books_dict.update({str(Id): {"books_title": line.replace("\n", ""), "lender_name": "", "Issue_data": "", "Status": "Available"}})
            Id = Id+1



    def display_books(self): 
        print("________________________________List of Books________________________________")
        print("Books ID", "\t", "Title", "\t\t\t", "Status")
        print("_____________________________________________________________________________")
        for key, value in self.books_dict.items(): 
            print(key, "\t", value.get("books_title")," - [ ", value.get("Status") , " ] ")

    def Issue_books(self):
        books_id = input("Enter Books ID : ")
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if books_id in self.books_dict.keys():
            if not self.books_dict[books_id]['Status'] == 'Available':
                print(f"This book is already issued to {self.books_dict[books_id]['lender_name']} on {self.books_dict[books_id]['lend_date']}")
                return self.lend_books()
            elif self.books_dict[books_id]['Status'] == 'Available':
                your_name = input("Enter Your Name : ")
                self.books_dict[books_id]['lender_name'] = your_name
                self.books_dict[books_id]['lend_date'] = current_date
                self.books_dict[books_id]['Status']= 'Already Issued'
                print("Book Issued Successfully !!!\n")
        else:
            print("Book ID Not Found !!!")
            return self.Issue_books()

    def add_books(self):
        new_books = input("Enter book's title: ")
        if new_books == "":
            return self.add_books()
        elif len(new_books) > 30:
            print("Book's title is very long!")
            return self.add_books()
        else: 
            with open(self.list_of_books, "a") as b:
                b.writelines(f"{new_books}\n")
            self.books_dict.update({str(int(max(self.books_dict))+1):{'books_title':new_books,'lender_name':'','lend_date':'', 'Status':'Available'}})
            print(f"The '{new_books}' has been added successfully !!!")

    def return_books(self):
        books_id = input("Enter books ID: ")
        if books_id in self.books_dict.keys(): 
            if self.books_dict[books_id]['Status']== "Available":
                print("This Book is already available")
                return self.return_books()
            elif not self.books_dict[books_id]['Status'] == 'Available':
                self.books_dict[books_id]['lender_name'] = ''
                self.books_dict[books_id]['lend_date'] = ''
                self.books_dict[books_id]['Status']= 'Available'
                print("Successfully Updated !!!\n")
        else:
            print("Book ID Not Found !!!")


if __name__ == "__main__":
    try:
        mylms = LMS("list_of_books.csv", "Python's")
        press_key_list = {"D": "Display Books", "I": "Issue Books", "A": "Add Books", "R": "Return Books", "Q": "Quit"}    
        
        key_press = False
        while not (key_press == "q"):
            print(f"\n----------Welcome To {mylms.library_name}'s Library Management System---------\n")
            for key, value in press_key_list.items():
                print("Press", key, "To", value)
            key_press = input("Press Key : ").lower()
            if key_press == "i":
                print("\nCurrent Selection : ISSUE BOOK\n")
                mylms.Issue_books()
                
            elif key_press == "a":
                print("\nCurrent Selection : ADD BOOK\n")
                mylms.add_books()

            elif key_press == "d":
                print("\nCurrent Selection : DISPLAY BOOKS\n")
                mylms.display_books()
            
            elif key_press == "r":
                print("\nCurrent Selection : RETURN BOOK\n")
                mylms.return_books()
            elif key_press == "q":
                break
            else:
                continue
    except Exception as e:
        print("Something went wrong. Please check. !!!")  


# l =  LMS("List_of_books.csv", "Python's Library")
# print(l.display_books())