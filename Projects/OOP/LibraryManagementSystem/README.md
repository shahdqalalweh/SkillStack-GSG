# 📚 Library Management System – Python OOP Project

> **يا أستاذ حاتم، بدي 100% العلامة 😁❤️**

---

## 📌 Overview

This is a simple **Library Management System** built in Python using **Object-Oriented Programming (OOP)** principles. It simulates a library where users can borrow, return, and reserve items (Books, Magazines, DVDs). The system reads and writes data using JSON files, supports abstraction, interfaces, exception handling, and custom exceptions.

---

## 🧱 Project Structure

```
LibraryManagementSystem/
│
├── main.py
├── items.json
├── users.json
│
├── models/
│   ├── library_item.py
│   ├── book.py
│   ├── magazine.py
│   ├── dvd.py
│   ├── reservable.py
│   ├── user.py
│   └── library.py
│
└── exceptions/
    ├── item_not_found.py
    ├── user_not_found.py
    ├── item_not_available.py
    └── reservation_error.py
```

---

## 💡 Features

- View all items in the library
- Search by ID
- Borrow and return items
- Reserve books and DVDs
- Persistent data using `items.json` and `users.json`
- Input validation & custom error handling

---

## 🧠 OOP Concepts Used

| Concept             | How it’s applied                                                |
|---------------------|-----------------------------------------------------------------|
| Abstraction         | `LibraryItem` is an abstract class                             |
| Interface (ABC)     | `Reservable` is an abstract interface with `reserve()` method  |
| Inheritance         | `Book`, `Magazine`, and `DVD` inherit from `LibraryItem`       |
| Polymorphism        | Items implement their own `display_info()`                     |
| Exception Handling  | Handled via try-except blocks                                  |
| Custom Exceptions   | E.g., `UserNotFoundError`, `ItemNotFoundError`                 |
| File Handling       | JSON read/write via `load_data()` and `save_data()`            |

---

## 👥 Users Example (users.json)

```json
[
  { "id": "U001", "name": "omar", "borrowed_items": [] },
  { "id": "U002", "name": "ahmad", "borrowed_items": [] },
  { "id": "U003", "name": "fatima", "borrowed_items": [] },
  { "id": "U004", "name": "mohammed", "borrowed_items": [] }
]
```

---

## 📖 Items Example (items.json)

```json
[
  {
    "id": "B001",
    "title": "Clean Code",
    "author": "Robert C. Martin",
    "type": "Book",
    "available": true
  },
  {
    "id": "D001",
    "title": "Artificial Intelligence: The Future",
    "author": "Layla Al-Zein",
    "type": "DVD",
    "available": true
  }
]
```

---

## ▶️ How to Run

1. Clone or download the project.
2. Make sure `items.json` and `users.json` are in the root directory.
3. Run the program:

```bash
python main.py
```

4. Choose from the CLI menu:

```
1. View items
2. Borrow item
3. Return item
4. Reserve item
5. Exit and save
```

---

## 🧪 Sample Session

```bash
Welcome to the Library System
1. View items
2. Borrow item
3. Return item
4. Reserve item
5. Exit and Save
```

---
