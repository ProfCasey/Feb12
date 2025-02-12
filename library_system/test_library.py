# File: test_library.py
from datetime import datetime, timedelta
from book import Book
from dvd import DVD
from library import Library

def test_library():
    # Create a library
    library = Library("Community Library")
    
    # Create some books and DVDs
    book1 = Book("The Hobbit", "B001", "J.R.R. Tolkien", 295)
    book2 = Book("Think Python", "B002", "Downey", 400)
    dvd1 = DVD("Godzilla Minus One", "D001", "Yamazaki", 136)
    
    # Add items to library
    library.add_item(book1)
    library.add_item(book2)
    library.add_item(dvd1)
    
    # Test checking out items
    print("\nTesting check out:")
    today = datetime.now()
    due_date = today + timedelta(days=14)  # Due in 14 days
    book1.check_out(due_date)
    print(book1)
    
    # Test searching
    print("\nSearching for 'Python':")
    python_items = library.find_items_by_title("Python")
    for item in python_items:
        print(item)
    
    # Test getting checked out items
    print("\nChecked out items:")
    checked_out = library.get_all_checked_out()
    for item in checked_out:
        print(item)

if __name__ == '__main__':
    test_library()