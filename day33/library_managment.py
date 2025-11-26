class Library:
    def __init__(self):
        self.books=[]
        self.no_of_books=0
    def add_book(self,add):
        self.books.append(add)
    def count(self):
        self.no_of_books=0
        for i in self.books:
            self.no_of_books+=1
    def show(self):
        if len(self.books)==0:
            print("Nothing in Library")
        else:
            for ind,books in enumerate(self.books,1):
                 print(f"{ind} : {books}")
lib=Library()
lib.add_book("Python Basics")
lib.add_book("Deep Learning")
lib.add_book("Machine learning")
lib.show()
lib.count()
print(f"\nTotal book in library : {lib.no_of_books}")

