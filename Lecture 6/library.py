class Book:
    total_books = 0

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.__price = price
        self.__is_issued = False
        Book.total_books += 1
        self.book_id = Book.total_books

    def get_price(self):
        return self.__price
    
    def set_price(self, new_price):
        if new_price < 0:
            print('Price cannot be negative')
        else:
            self.__price = new_price

    def issue_book(self):
        if self.__is_issued:
            print(f"'{self.title}' is already issued")
        else:
            self.__is_issued = True
            print(f"'{self.title}' issued successfully")

    def return_book(self):
        if not self.__is_issued:
            print(f"'{self.title}' is available in the library")
        else:
            self.__is_issued = False
            print(f"'{self.title}' is successfully returned")

    def display_info(self):
        status = 'Issued' if self.__is_issued else 'Available'
        print(f"[ID: {self.book_id}] '{self.title}' by {self.author} | Rs. {self.__price} | {status}")

    @staticmethod
    def is_valid_price(price):
        return price > 0

    @classmethod
    def get_total_books(cls):
        return cls.total_books


book1 = Book('Python Course', 'Eric', 599)
book2 = Book('Atomic Habits', 'James Clear', 399)

book1.display_info()
book2.display_info()
print('Total Books:', Book.get_total_books())

book1.issue_book()
# book1.issue_book()  # this will throw error
book1.display_info()

book1.return_book()
book2.set_price(499)
book2.display_info()
book1.display_info()
print('Book2 price:', book2.get_price())