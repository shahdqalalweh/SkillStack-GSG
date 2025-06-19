from models.library_item import LibraryItem

class Magazine(LibraryItem):
    def display_info(self):
        return f"[Magazine] {self.title} by {self.author}"