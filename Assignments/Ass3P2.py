"""
Prime Number Analyzer
Let the user input a range of numbers.
Use a function to check if a number is prime.
Write all prime numbers in that range to a file, one per line.
"""
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:
            return False
    return True


start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

output_file = "prime_numbers.txt"


with open(output_file, 'w') as file:
    for number in range(start, end + 1):
        if is_prime(number):
            file.write(f"{number}\n")

print(f"Prime numbers from {start} to {end} have been written to '{output_file}'")
