from product import Product

class Candy(Product):
    def __init__(self, name, price, flavor):
        super().__init__(name, price)
        self.flavor = flavor

    def display_info(self):
        super().display_info()
        print(f"Flavor: {self.flavor}")