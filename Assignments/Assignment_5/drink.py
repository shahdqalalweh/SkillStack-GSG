from product import Product

class Drink(Product):
    def __init__(self, name, price, volume):
        super().__init__(name, price)
        self.volume = int(volume)

    def display_info(self):
        super().display_info()
        print(f"Volume: {self.volume}ml")