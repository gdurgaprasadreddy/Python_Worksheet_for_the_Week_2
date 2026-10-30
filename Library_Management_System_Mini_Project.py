class Library:
    def __init__(self):
        self.books = [
            {"book_id": 123, "title": "Wings of Fire",
             "author": "A.P.J.Abdul Kalam", "available": True},
            {"book_id": 456, "title": "Gitanjali",
             "author": "Rabindranath Tagore", "available": True},
        ]

    def add_book(self):
        book_id = int(input("Enter Book ID:"))

        for book in self.books:
            if book["book_id"] == book_id:
                print("Book ID already exists")
                return

        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        new_book = {
            "book_id": book_id,
            "title": title,
            "author": author,
            "available": True
        }
        self.books.append(new_book)
        print("Book added successfully")

    def issue_book(self):
        book_id = int(input("Enter Book ID to issue: "))

        for book in self.books:
            if book["book_id"] == book_id:
                if book["available"]:
                    book["available"] = False
                    print("Book issued successfully")
                else:
                    print("Book is already issued")
                return

        print("Book not found")

    def return_book(self):
        book_id = int(input("Enter Book ID to return: "))

        for book in self.books:
            if book["book_id"] == book_id:
                if not book["available"]:
                    book["available"] = True
                    print("Book returned successfully")
                else:
                    print("This book is already available")
                return

        print("Book not found")

    def display_books(self):
        print("\n=== AVAILABLE BOOKS ===")
        found = False

        for book in self.books:
            if book["available"]:
                print("Book ID:", book["book_id"])
                print("Title:", book["title"])
                print("Author:", book["author"])
                print("--------------------")
                found = True

        if not found:
            print("No books are currently available.")

library = Library()

while True:

    print("\n=== LIBRARY MANAGEMENT SYSTEM ===")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Display Available Books")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            library.add_book()

        elif choice == 2:
            library.issue_book()

        elif choice == 3:
            library.return_book()

        elif choice == 4:
            library.display_books()

        elif choice == 5:
            print("Thank you for using the Library Management System!")
            break

        else:
            print("Invalid choice! Please select 1 to 5.")

    except ValueError:
        print("Invalid input! Please enter a valid number.")
