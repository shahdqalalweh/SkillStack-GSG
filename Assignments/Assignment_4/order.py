class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def total(self):
        return sum(item.price for item in self.items)

    def __str__(self):
        item_list = "\n".join(f"- {item}" for item in self.items)
        return f"{item_list}\nTotal: ${self.total():.2f}"
