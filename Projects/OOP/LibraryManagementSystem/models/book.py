from models.library_item import LibraryItem
from models.reservable import Reservable

class Book(LibraryItem, Reservable):
    def display_info(self):
        return f"[Book] {self.title} by {self.author}"

    def reserve(self, user):
        if not self.available:
            raise Exception("Book already reserved.")
        self.available = False