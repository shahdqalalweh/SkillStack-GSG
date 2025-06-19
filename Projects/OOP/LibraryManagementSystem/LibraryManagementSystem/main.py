from models.library import Library

lib = Library()
lib.load_data()

while True:
    print("\n--- Library Menu ---")
    print("1. View items")
    print("2. Borrow")
    print("3. Return")
    print("4. Reserve")
    print("5. Exit")
    choice = input("Choose: ")

    if choice == "1":
        for item in lib.items.values():
            print(item.display_info(), "| Available:", item.available)
    elif choice == "2":
        try:
            uid = input("User ID: ")
            iid = input("Item ID: ")
            lib.borrow_item(uid, iid)
            print("Borrowed successfully.")
        except Exception as e:
            print("Error:", e)
    elif choice == "3":
        try:
            uid = input("User ID: ")
            iid = input("Item ID: ")
            lib.return_item(uid, iid)
            print("Returned successfully.")
        except Exception as e:
            print("Error:", e)
    elif choice == "4":
        try:
            uid = input("User ID: ")
            iid = input("Item ID: ")
            lib.reserve_item(uid, iid)
            print("Reserved successfully.")
        except Exception as e:
            print("Error:", e)
    elif choice == "5":
        lib.save_data()
        print("Data saved. Goodbye!")
        break