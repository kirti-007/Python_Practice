class Library:
    def __init__(self):
        self.books = {}
        self.noofbooks = 0

    def add_book(self, title, author):
        book_id = len(self.books) + 1
        self.books[book_id] = {"title": title, "author": author}
        print(f"Book '{title}' by {author} added with ID {book_id}")
        self.noofbooks = len(self.books)

    def display_books(self):
        print(f"\nWelcome to Library.....\n")
        if not self.books:
            print("No books in the library.")
        else:
            print(f"There are {self.noofbooks} number of books available in the Library")
            print("Books:-")
            for book_id, book_info in self.books.items():
                print(f"ID: {book_id}, Title: {book_info['title']}, Author: {book_info['author']}")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Book '{removed_book['title']}' by \"{removed_book['author']}\" removed.")
        else:
            print(f"Book with ID {book_id} not found.")


library = Library()

while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Remove Book")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        library.add_book(title, author)

    elif choice == "2":
        library.display_books()

    elif choice == "3":
        book_id = int(input("Enter the ID of the book to remove: "))
        library.remove_book(book_id)

    elif choice == "4":
        print("\nThanks for coming. Goodbye!\n")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
