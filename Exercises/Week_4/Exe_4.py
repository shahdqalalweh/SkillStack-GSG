 #  Immutable vs Mutable Variables
    # Mutable => قابل للتعديل والتغيير
    # Immutable => غير قابل للتعديل ولا التغيير


# Immutable examples
int_value = 42
# int_value[0] = 5 # TypeError: 'int' object does not support item assignment
float_value = 3.14
# float_value[0] = 1 # TypeError: 'float' object does not support item assignment
name = "Fido"
print(name[0]) # Output: 'F'
# name[0] = "R" # TypeError: 'str' object does not support item assignment
tuple_value = (1, 2, 3)
# tuple_value[0] = 100 # TypeError: 'tuple' object does not support item assignment


# Mutable examples
tricks = ["sit", "roll"]
tricks.append("stay")
print(tricks) # Output: ['sit', 'roll', 'stay']
dog_info = {"name": "Buddy", "age": 5}
dog_info["breed"] = "Labrador"
print(dog_info) # Output: {'name': 'Buddy', 'age': 5, 'breed': 'Labrador'}
commands = {"sit", "stay"}
commands.add("roll")
print(commands) # Output: {'stay', 'sit', 'roll'} (order may vary)