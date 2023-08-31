class Library:

    def __init__(self, list1):
        self.books = list1

    def display_books(self):
        for book in self.books:
            print(book)

    def lend_book(self, book_name):
        if book_name in self.books:
            print("You have received a Book : "+book_name)
        else:
            print("Book not found")

        self.books.remove(book_name)

    def add_book(self, book_name):
        self.books.append(book_name)


class Customer:
    def request_book(self):
        book_name = input("Enter a book you want")
        self.book_name = book_name
        return self.book_name


    def return_book(self):
        book_name = input("Enter a book to return")
        self.book_name = book_name
        return self.book_name


books_list = ["RICH DAD POOR DAD", "IKIGAI", "MELUHA"]
lib = Library(books_list)
option = 0

if not option:
    option = int(input("Enter a option"))
if option == 2:
    print("Request a book : ")
    cust = Customer()
    lib.lend_book(cust.request_book())
if option == 3:
    print("Return a book : ")
    cust = Customer()
    lib.add_book(cust.return_book())
    lib.display_books()
else:
    print("select at lease an option")
