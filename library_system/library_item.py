class LibraryItem:
    """Base class for all library items."""
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.checked_out = False
        self.due_date = None
    
    def __str__(self):
        status = "checked out" if self.checked_out else "available"
        return f"{self.title} ({self.item_id}) - {status}"
    
    # Your turn: Add a check_out method that takes a due_date parameter
    # and updates the checked_out status
    
    # Your turn: Add a return_item method that resets the checked_out
    # status and due_date