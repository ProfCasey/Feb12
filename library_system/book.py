from library_item import LibraryItem

class Book(LibraryItem):
    """Represents a book in the library."""
    def __init__(self, title, item_id, author, pages):
        super().__init__(title, item_id)
        self.author = author
        self.pages = pages
        
    def __str__(self):
        return f"Book: {super().__str__()} by {self.author}"
    
    #Your Turn: Add a method is_long that