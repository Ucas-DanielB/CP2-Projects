#  Daniel Blanco

# Personal Library Management Program

# Define a function to display the menu
def display_menu():
    print("\n--- Personal Library Menu ---")
    print("1. Add a new book")
    print("2. Display all books")
    print("3. Search for a book")
    print("4. Remove a book")
    print("5. Exit")

# Define a function to add a new book
def add_book(library):
    title = input("Enter the book title: ").strip()
    author = input("Enter the book author: ").strip()
    genres = input("Enter the book genres (comma-separated): ").strip()
    year = input("Enter the year of publication: ").strip()
    
    genres_set = set(genres.split(","))
    
    library.append({
        "title": title, 
        "author": author, 
        "genres": genres_set, 
        "year": year
    })
    print(f"Book '{title}' by {author} added successfully!")

# Define a function to display all books (Simple or Detailed)
def display_books(library):
    if not library:
        print("No books in the library.")
        return
    
    choice = input("View books in (1) Simple list or (2) Detailed list? Enter 1 or 2: ").strip()
    
    print("\n--- Library Catalog ---")
    for idx, book in enumerate(library, 1):
        if choice == "1":  # Simple list
            print(f"{idx}. {book['title']} by {book['author']}")
        elif choice == "2":  # Detailed list
            print(f"{idx}. Title: {book['title']}")
            print(f"   Author: {book['author']}")
            print(f"   Genres: {', '.join(book['genres'])}")
            print(f"   Year: {book['year']}")
            print("---------------------------")
        else:
            print("Invalid choice. Showing simple list by default.")
            print(f"{idx}. {book['title']} by {book['author']}")

# Define a function to search for a book
def search_book(library):
    query = input("Enter the book title or author to search: ").strip().lower()
    found_books = [book for book in library if query in book['title'].lower() or query in book['author'].lower()]
    
    if found_books:
        print("\n--- Search Results ---")
        for book in found_books:
            print(f"{book['title']} by {book['author']} (Genres: {', '.join(book['genres'])}, Year: {book['year']})")
    else:
        print("No books found matching your search.")

# Define a function to remove a book
def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip()
    for book in library:
        if book['title'].lower() == title.lower():
            library.remove(book)
            print(f"Book '{title}' removed successfully!")
            return
    print(f"No book found with the title '{title}'.")

# Main function to run the program
def main():
    library = []  # List to store the library catalog
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            add_book(library)
        elif choice == "2":
            display_books(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            remove_book(library)
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Run the program
if __name__ == "__main__":
    main()
