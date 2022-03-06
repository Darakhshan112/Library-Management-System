
class Admin:

    def __init__(self,adminId,password):
        self.admin=adminId
        self.password=password

    def checkCredentials(self,adminId,password):
        if (self.admin==adminId and self.password == password):
            return True
        else:
            return False

class Student:
    def __init__(self,userId,password,name):
        self.user=userId
        self.password=password
        self.name=name
       
    def checkCredentials(self,userId,password):
        if (self.user==userId and self.password == password):
            return True
        else:
            return False
        
    def requestBook(self,bookname):
        self.book=bookname
        return (self.book)

    def returnBook(self,bookname):
        self.book=bookname
        return self.book


class Library:
    def __init__(self,availableBooks):
        self.books=availableBooks
        self.borrowerDetails={}

    def displayBooks(self):
        print("Books \t Copies\n")

        for key,val in self.books.items():
            print(f"{key} \t {val}")
    
    def addBooks(self,name,copy):
       
        self.books.update({
            name:copy})

    def showBorrowers(self):
        print(f"The borrowers of Our Library are\n{self.borrowerDetails}")

    def deleteBooks(self,bookName):
        if bookName in self.books.keys():
            self.books.pop(bookName)
            print(f"\nThe book {bookName} is deleted from our Library")
        else:
            print(f"\nNo {bookName} is available in our Library")

    def issueBook(self,borrowername,bookname):
        if bookname in self.books.keys():
            if self.books[bookname]>0:          
                self.books[bookname]=self.books[bookname]-1
                print(f"\n{bookname} is issued to you")
                if borrowername in self.borrowerDetails.keys():
                    self.borrowerDetails[borrowername].append(bookname)
                else:
                    self.borrowerDetails.update({
                        borrowername:[bookname]})             
            else:
                print(f"Sorry! Currently,no copy of {bookname} is available.")
        else:
            print(f"Sorry! No {bookname} book is available in our Library.")

    def returnBook(self,borrowername,bookname):
        print(borrowername,bookname,self.books.keys())
        if bookname in self.books.keys():
            if bookname in self.borrowerDetails[borrowername]:
                self.books[bookname]=self.books[bookname]+1
                while bookname in self.borrowerDetails[borrowername]:
                    self.borrowerDetails[borrowername].remove(bookname) 
                print(f"You returned the {bookname} book")
            else:
                print(f"{bookname} book is not borrowed by you")
        else:
            print(f"{bookname} book is not borrowed from our Libraray")

l=Library( {
                    "Python":2,
                    "C++":3
                })
s= Student("user","us","saad")
a=Admin("admin","ad")

while(True):
    try:
        n=input("Are you a Student or Library Admin?\nPress (s) for Student and Press (a) for Admin:")
        if(n.lower()=='a'):
            admin=input("Admin! Enter Your Username:")
            adminPass=input("Admin! Enter Your Password:")
            if(a.checkCredentials(admin,adminPass)):
                print("\n\t\t\tWelcome to Our Library")
                while(True):        
                    menuInput=int(input("\n1. Dispaly Books(Press 1)\n2. Add Books/update(Press 2)\n3. Delete Books(Press 3)\n4. Display Borrowers(Press 4)\n5. To exit(Press 5)\n\nEnter your Choice:"))     

                    if (int(menuInput)==1):
                        l.displayBooks()

                    elif(int(menuInput)==2):
                        noOfBooks=input("Enter number of books you want to add/update:")
                        for i in range(int(noOfBooks)):
                            nameOfBook=input("Enter Book Name:")
                            noOfCopies=input(f"Enter No of copies of {nameOfBook}:")
                            l.addBooks(nameOfBook.capitalize(),noOfCopies)

                    elif(int(menuInput)==3):
                        noOfBooks=input("Enter number of books you want to delete:")
                        for i in range(int(noOfBooks)):
                            nameOfBook=input("Enter Book Name:")
                            l.deleteBooks(nameOfBook.capitalize())

                    elif(int(menuInput)==4):
                        l.showBorrowers()
                        
                    elif(int(menuInput)==5):
                        break

                    else:
                        print("Choose right option")
            else:
                print("Username or password is Invalid. Try again....")

        elif (n.lower()=='s'):
            username=input("User! Enter Your Username:")
            userPassword=input("User! Enter Your Password:")
        
            if(s.checkCredentials(username,userPassword)):
                print("\n\t\t\tWelcome to Our Library")
                while(True):
                    menuInput=input("\n1. Dispaly Books(Press 1)\n2. Request(Press 2)\n3. Return(Press 3)\n4. Exit(Press 4)\n\nEnter your Choice:")
                    menuInput=int(menuInput)

                    if (menuInput==1):
                        l.displayBooks()

                    elif(menuInput==2):
                        nameOfBook=input("\nEnter book name:")
                        l.issueBook(s.name,s.requestBook(nameOfBook.capitalize()))
                    
                    elif(menuInput==3):
                        nameOfBook=input("\nEnter book name:")
                        l.returnBook(s.name,nameOfBook.capitalize())
                        
                    else:
                        break
            else:
                print("Username or password is Invalid. Try again....")
        else:
            print("Choose right option")
        
    except Exception as e:
        print(f"There is some exception occured{e}")

                    
            
