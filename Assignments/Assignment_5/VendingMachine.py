from drink import Drink
from snack import Snack
from candy import Candy

def load_products_from_file(filename):
    products = []
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) != 4:
                    continue
                category, name, price, extra = parts
                if category == "Drink":
                    products.append(Drink(name, price, extra))
                elif category == "Snack":
                    products.append(Snack(name, price, extra))
                elif category == "Candy":
                    products.append(Candy(name, price, extra))
    except FileNotFoundError:
        print("Error: File not found.")
    return products

def show_menu(products):
    print("Welcome to the Python Vending Machine!\n")
    print("Please select what you want:")
    for idx, product in enumerate(products, 1):
        print(f"{idx}. {type(product).__name__} - {product.name}")

    try:
        choice = int(input("\n> "))
        if 1 <= choice <= len(products):
            print("\nProduct Information:")
            products[choice - 1].display_info()
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    products = load_products_from_file("products.txt")
    if products:
        show_menu(products)
    else:
        print("No products loaded.")