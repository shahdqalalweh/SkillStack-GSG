from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, item_id, title, author):
        self.item_id = item_id
        self.title = title
        self.author = author
        self.available = True

    @abstractmethod
    def display_info(self):
        pass

    def check_availability(self):
        return self.available