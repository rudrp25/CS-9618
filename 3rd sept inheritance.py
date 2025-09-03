import datetime as dt
class LibraryItem:

    def __init__(self, t, a, i):
        self.__Title = t
        self.__AuthorArtist = a
        self.__ItemID = i
        self.__OnLoan = False
        self.__DueDate = dt.date.today()

    def GetTitle(self):
        return(self.__Title)

    def Borrowing(self):
        self.__OnLoan = True
        self.__DueDate = self.__DueDate + dt.timedelta(weeks=3)

    def Returning(self):
        self.__OnLoan = False

    def PrintDetails(self):
        print(self.__Title, '',self.__AuthorArtist,'')
        print(self.__ItemID, '', self.__OnLoan, '', self.__DueDate)

class Book(LibraryItem):

    def __init__(self,t,a,i):
        LibraryItem.__init__(self, t, a, i)
        self.__IsRequested = False
        self.__RequestedBy = 0

    def GetIsRequested(self):
        return(self.__IsRequested)

    def SetRequested(self):
        self.__IsRequested = True

class CD(LibraryItem):

    def __init__(self):
        LibraryItem.__init__(self,t,a,i)
        self.__Genre = ""

    def GetGenre(self):
        return(self.__Genre)

    def SetGenre(self, g):
        self.__Genre = g


books = []
cd = []

for i in range(0,5):
    title = input("Enter title name: ")
    author = input("Enter author name: ")
    id = input("Enter book ID: ")
    book1 = [Book(title,author,id)]
    books.append(book1)



for i in range(0,6):
    title = input("Enter title name: ")
    author = input("Enter author name: ")
    id = input("Enter CD ID: ")
    cd1 = [CD(title,author,id)]
    cd.append(cd1)