#Assuming there are 2 copies of each book
#Assuming the fine for extending the deadline is 5rs per day
import datetime
booksname2=''
class Library:
    c=1
    def __init__(self,Listofbooks,nameoflib,id1,auth_name,publ_date,coun):
        self.listofbooks = Listofbooks
        self.listofbooks2=Listofbooks
        self.nameoflibrary = nameoflib
        self.lendbooks = dict()
        self.lendbooks2=dict()
        self.id=id1
        self.author_name=auth_name
        self.pub_date=publ_date
        self.reservebook=dict()
        self.counter=coun

    def displaybook(self):
        print("We have a collection of Books: (The number to the left of the name represents its ID number)")
        count = 1151
        for book in self.listofbooks:
            print("{}: {}".format(count, book))
            count += 1
        print('Note the list of reserved books(You cannot issue them now,come back later)')
        print(self.reservebook)

    def lendbook(self, username,bookname,rackno):
        if bookname not in self.listofbooks:
            print("Book is not present in our collection")
        elif bookname not in self.lendbooks.keys():
            self.lendbooks.update({bookname: username})
            self.counter += 1
            if self.counter >= 6:
                print('You cannot issue more than 5 books')
                exit()
            print(f"Now you can take this book from Rack no. {rackno}")
        elif bookname not in self.lendbooks2.keys():
            self.lendbooks2.update({bookname: username})
            self.counter+=1
            if self.counter>=6:
                print('You cannot issue more than 5 books')
                exit()
            print(f"Now you can take this book from Rack no. {rackno}")
        else:
            print(f"Book1 is already taken by {self.lendbooks[bookname]}")
            print(f"Book2 is already taken by {self.lendbooks2[bookname]}")
            reserve=int(input('Enter 1 if you want to reserve this book\n'))
            if reserve==1:
                self.reservebook.update({bookname: username})
                print('Your book  has been reserved!!')
        confirm=input('Confirm with a Y if you are issuing a reserved book or else press n ')
        if confirm=='Y' or confirm=='y':
            self.reservebook.pop(bookname)

    def returnbook(self, booksname,username3):
        self.lendbooks.pop(booksname)
        self.lendbooks2.pop(booksname)
        print("Book has been returned..!!")

print("Welcome to Prateek's Library")
prateek = Library(['Letting go','Fear of flying','The adventures of Tom Sawyer','In Search of Lost Time','War and Peace','Hamlet'], "Python sample Library",[1151,1152,1153,1154,1155,1156],['David R. Hawkins','Erica Jong','Mark Twain','Marcel Proust','Leo Tolstoy','William Shakespeare'],[1962,1973,1876,1913,1867,1600],0)
counter=0
co=1
while True:
    print("\nWhat would you like to do??..Choose any one operation")
    print(f"1: Display Book \n2: Issue Book  \n3: Return Book \n4: Issue reserved book\n5: Exit\n")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        prateek.displaybook()
    elif choice == 2:
        user_name = input("Enter name of user:")
        c2=int(input('Enter 1 if you want to search by name\n'
                     '      2 if you want to search by ID\n'
                     '      3 if you want to search by Authors name\n'
                     '      4 if you want to search by publication year\n'))
        if c2==1:
            book_name = input("Enter name of book:")
            prateek.lendbook(user_name, book_name,1)
        elif c2==2:
            id_no=int(input('Enter the id number '))
            if id_no==1151:
                prateek.lendbook(user_name,'Letting go',1)
            elif id_no==1152:
                prateek.lendbook(user_name, 'Fear of flying',2)
            elif id_no==1153:
                prateek.lendbook(user_name, 'The adventures of Tom Sawyer',3)
            elif id_no ==1154:
                prateek.lendbook(user_name, 'In Search of Lost Time',4)
            elif id_no==1155:
                prateek.lendbook(user_name, 'War and Peace',5)
            elif id_no==1156:
                prateek.lendbook(user_name, 'Hamlet',6)

        elif c2==3:
            auth_name2=input('Enter the authors name ')
            if auth_name2=='David R. Hawkins':
                prateek.lendbook(user_name, 'Letting go',1)
            elif auth_name2=='Erica Jong':
                prateek.lendbook(user_name, 'Fear of flying',2)
            elif auth_name2=='Mark Twain':
                prateek.lendbook(user_name, 'The adventures of Tom Sawyer',3)
            elif auth_name2=='Marcel Proust':
                prateek.lendbook(user_name, 'In Search of Lost Time',4)
            elif auth_name2=='Leo Tolstoy':
                prateek.lendbook(user_name, 'War and Peace',5)
            elif auth_name2=='William Shakespeare':
                prateek.lendbook(user_name, 'Hamlet',6)
        elif c2==4:
            pub_yr=int(input('Enter the year of publication'))
            if pub_yr==1962:
                prateek.lendbook(user_name, 'Letting go',1)
            elif pub_yr==1973:
                prateek.lendbook(user_name, 'Fear of flying',2)
            elif pub_yr==1876:
                prateek.lendbook(user_name, 'The adventures of Tom Sawyer',3)
            elif pub_yr==1913:
                prateek.lendbook(user_name, 'In Search of Lost Time',4)
            elif pub_yr==1867:
                prateek.lendbook(user_name, 'War and Peace',5)
            elif pub_yr==1600:
                prateek.lendbook(user_name, 'Hamlet',6)
        else:
            print('Sorry wrong input!')
        tday=datetime.date.today()


    elif choice == 3:
        username2=input('Enter your name as entered while issuing the book ')
        name_book = input("Enter name of book:")
        tdelta=datetime.date.today()-tday
        if int(tdelta.days) >10:
            print(f'Fine to be paid is Rupees {(int(datetime.date.today())-10)*5}')
        prateek.returnbook(name_book,username2)
    elif choice == 4:
        user_name3 = input('Enter your name ')
        bookname2 = input('Enter the name of your reserved book ')
        prateek.lendbook(user_name3, bookname2, 1)
    elif choice == 5:
        print("Thank you..!!")
        exit()
    else:
        print('Sorry wrong input,try again')



