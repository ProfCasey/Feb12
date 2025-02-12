from library_item import LibraryItem

class DVD(LibraryItem):
    """Represents a DVD in the library."""
    def __init__(self, title, item_id, director, runtime):
        super().__init__(title, item_id)
        self.director = director
        self.runtime = runtime  # in minutes
        
    def __str__(self):
        return f"DVD: {super().__str__()} directed by {self.director}"