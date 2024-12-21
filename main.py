class Library:
    book_list = []

    @classmethod
    def entry_book(self, book):
        self.book_list.append(book)

    @classmethod
    def view_all_books(self):
        if not self.book_list:
            print("No book is available")
        else:
            for book in self.book_list:
                print(book.view_book_info())


class Book:
    def __init__(self, book_id, title, author, availability):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = availability

    def borrow_book(self):
        if self.__availability:
            self.__availability = False
            return f"'{self.__title}' has been succesfully borrowed."
        else:
            return f"'{self.__title}' is not available for borrowing."

    def return_book(self):
        if not self.__availability:
            self.__availability = True
            return f"'{self.__title}' is returned and is now available for borrowing."
        else:
            return f"'{self.__title}' is available already!"

    def view_book_info(self):
        return f"ID: {self.__book_id}, Title: {self.__title}, Author: {self.__author}, Availability: {'Available' if self.__availability else 'Unavailable'}"

    # Getter
    def get_book_id(self):
            return self.__book_id


# Create 10 Book objects
book1 = Book(1, "1984", "George Orwell", True)
book2 = Book(2, "To Kill a Mockingbird", "Harper Lee", False)
book3 = Book(3, "Pride and Prejudice", "Jane Austen", True)
book4 = Book(4, "The Great Gatsby", "F. Scott Fitzgerald", True)
book5 = Book(5, "Moby-Dick", "Herman Melville", False)
book6 = Book(6, "War and Peace", "Leo Tolstoy", True)
book7 = Book(7, "The Catcher in the Rye", "J.D. Salinger", True)
book8 = Book(8, "The Hobbit", "J.R.R. Tolkien", False)
book9 = Book(9, "Crime and Punishment", "Fyodor Dostoevsky", True)
book10 = Book(10, "Brave New World", "Aldous Huxley", True)

# Add books to the Library
Library.entry_book(book1)
Library.entry_book(book2)
Library.entry_book(book3)
Library.entry_book(book4)
Library.entry_book(book5)
Library.entry_book(book6)
Library.entry_book(book7)
Library.entry_book(book8)
Library.entry_book(book9)
Library.entry_book(book10)

while True:
    print("\n-------- Welcome To The Library --------")
    print()
    print("1. View All Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")

    try:
        choice = int(input("\nEnter your choice: "))
        print("--------------------------\n")

        if choice == 1:
            Library.view_all_books()

        elif choice == 2:
            book_id = int(input("Enter The Book's ID: "))
            print()
            found = 0

            for b in Library.book_list:
                if book_id == b.get_book_id():
                    found = 1
                    print(b.borrow_book())

            if not found:
                print("Sorry the book is not in the library!")


        elif choice == 3:
            book_id = int(input("Enter The Book's ID: "))
            print()
            found = 0

            for b in Library.book_list:
                if book_id == b.get_book_id():
                    found = 1
                    print(b.return_book())

            if not found:
                print("Sorry the book is not in the library!")


        elif choice == 4:
            print("The Program Is Closing.\n")
            break

        else:
            print("Option is not available.")

    except ValueError:
        print("\nInvalid Option.")


book1.view_book_info()