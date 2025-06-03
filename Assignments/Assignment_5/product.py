class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = float(price)

    def display_info(self):
        print(f"Product: {self.name}, Price: ${self.price:.2f}")