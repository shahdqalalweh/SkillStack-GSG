class Restaurant:
    def __init__(self):
        self.menu = []
        self.orders = []

    def add_menu_item(self, item):
        self.menu.append(item)

    def get_menu(self):
        return self.menu

    def add_order(self, order):
        self.orders.append(order)

    def list_orders(self):
        for idx, order in enumerate(self.orders, 1):
            print(f"Order {idx}:\n{order}\n")
