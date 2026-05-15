def add_book(catalog, book_id, title, author, year):
    catalog.update( { book_id: (title,author,year) } )
    print(f"Book '{title}' added successfully.")

def borrow_book(catalog, borrowed_books, book_id):
    if book_id in catalog:
        if book_id not in borrowed_books:
            borrowed_books.append(book_id)
            print(f"{book_id} borrowed succesfully")
        else:
            print("The book is already borrowed")
    else:
        print("The book doesnot exist")

def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print(f"Book {book_id} returned successfully.")
    else:
        print("This book is not borrowed")

def register_member(members, member_id):
    members.add(member_id)
    print(f"Member {member_id} registered.")

def show_available(catalog, borrowed_books):
    for key in catalog:
        if key not in borrowed_books:
            available_books = catalog[key]
        print("Available books are : ",available_books)

def main():

    catalog = {}
    borrowed_books = []
    members = set()

    # Adding books
    print("-" * 7)

    add_book(catalog, 101, "Python Basics", "John Smith", 2020)
    add_book(catalog, 102, "AI Fundamentals", "David Lee", 2021)
    add_book(catalog, 103, "Data Science", "Sara Khan", 2019)
    add_book(catalog, 104, "Machine Learning", "Alan Roy", 2022)

    # Registering members
    print("-" * 7)

    register_member(members, 1)
    register_member(members, 2)
    register_member(members, 3)

    # Borrowing books
    print("-" * 7)

    borrow_book(catalog, borrowed_books, 101)
    borrow_book(catalog, borrowed_books, 103)

    # Returning one book
    print("-" * 7)

    return_book(borrowed_books, 101)

    # Showing available books
    print("-" * 7)

    show_available(catalog, borrowed_books)


main()
