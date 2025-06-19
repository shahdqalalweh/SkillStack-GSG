import json
import os
from models.book import Book
from models.magazine import Magazine
from models.dvd import DVD
from models.user import User
from exceptions.user_not_found import UserNotFoundError
from exceptions.item_not_found import ItemNotFoundError
from exceptions.item_not_available import ItemNotAvailableError
from exceptions.reservation_error import ReservationError

class Library:
    def __init__(self):
        self.items = {}
        self.users = {}

    def load_data(self):
        base_path = os.path.dirname(os.path.abspath(__file__))
        items_path = os.path.join(os.path.dirname(base_path), "items.json")
        users_path = os.path.join(os.path.dirname(base_path), "users.json")

        with open(items_path, "r", encoding="utf-8") as f:
            items_data = json.load(f)
            for i in items_data:
                if i["type"] == "Book":
                    item = Book(i["id"], i["title"], i["author"])
                elif i["type"] == "Magazine":
                    item = Magazine(i["id"], i["title"], i["author"])
                elif i["type"] == "DVD":
                    item = DVD(i["id"], i["title"], i["author"])
                item.available = i["available"]
                self.items[i["id"]] = item

        with open(users_path, "r", encoding="utf-8") as f:
            users_data = json.load(f)
            for u in users_data:
                user = User(u["id"], u["name"])
                user.borrowed_items = u["borrowed_items"]
                self.users[u["id"]] = user

    def save_data(self):
        base_path = os.path.dirname(os.path.abspath(__file__))
        items_path = os.path.join(os.path.dirname(base_path), "items.json")
        users_path = os.path.join(os.path.dirname(base_path), "users.json")

        items_data = []
        for item in self.items.values():
            items_data.append({
                "id": item.item_id,
                "title": item.title,
                "author": item.author,
                "type": item.__class__.__name__,
                "available": item.available
            })

        users_data = []
        for user in self.users.values():
            users_data.append({
                "id": user.user_id,
                "name": user.name,
                "borrowed_items": user.borrowed_items
            })

        with open(items_path, "w", encoding="utf-8") as f:
            json.dump(items_data, f)

        with open(users_path, "w", encoding="utf-8") as f:
            json.dump(users_data, f)

    def borrow_item(self, user_id, item_id):
        if user_id not in self.users:
            raise UserNotFoundError()
        if item_id not in self.items:
            raise ItemNotFoundError()
        user = self.users[user_id]
        item = self.items[item_id]
        if not item.available:
            raise ItemNotAvailableError()
        user.borrow_item(item)

    def return_item(self, user_id, item_id):
        user = self.users[user_id]
        item = self.items[item_id]
        user.return_item(item)

    def reserve_item(self, user_id, item_id):
        user = self.users[user_id]
        item = self.items[item_id]
        if hasattr(item, "reserve"):
            item.reserve(user)
        else:
            raise ReservationError("Item is not reservable.")