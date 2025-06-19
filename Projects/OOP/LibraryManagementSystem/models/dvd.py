from models.library_item import LibraryItem
from models.reservable import Reservable

class DVD(LibraryItem, Reservable):
    def display_info(self):
        return f"[DVD] {self.title} by {self.author}"

    def reserve(self, user):
        if not self.available:
            raise Exception("DVD already reserved.")
        self.available = False