from product import Product

class Snack(Product):
    def __init__(self, name, price, calories):
        super().__init__(name, price)
        self.calories = int(calories)

    def display_info(self):
        super().display_info()
        print(f"Calories: {self.calories} kcal")