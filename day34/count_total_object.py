class Books:
    total=0
    def __init__(self,book_name,writer):
        self.book_name=book_name
        self.writer=writer
        Books.total+=1
    @classmethod
    def object_count(cls):
       return cls.total
b1=Books("Machine learning","ME")
b2=Books("Linux","ME")
b3=Books("Deep learning","ME")

print(Books.object_count())