class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_items = []

    def borrow_item(self, item):
        if not item.available:
            raise Exception("Item not available.")
        item.available = False
        self.borrowed_items.append(item.item_id)

    def return_item(self, item):
        item.available = True
        self.borrowed_items.remove(item.item_id)