class Calculator:
    def add(self, *args):
        result = 0
        for number in args:
             result += number
        return result
    
calc = Calculator()
print(calc.add(1, 2)) # Output: 3
print(calc.add(1, 2, 3, 4, 5)) # Output: 15