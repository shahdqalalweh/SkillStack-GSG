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




"""
 Word Counter
Ask the user for a file name.
Count and display the number of words in the file.
Also, identify the most frequent word and how many times it appears.

"""

file_name = input("Enter the file name: ")

try:
   
    with open(file_name, 'r') as file:
        text = file.read()

   
    import string
    text = text.lower()
    for ch in string.punctuation:
        text = text.replace(ch, "")

    words = text.split()

    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    total_words = len(words)

    most_common_word = None
    max_count = 0
    for word, count in word_freq.items():
        if count > max_count:
            most_common_word = word
            max_count = count

    print(f"Total words: {total_words}")
    print(f"Most frequent word: '{most_common_word}' appeared {max_count} times")

except FileNotFoundError:
    print("Error: File not found.")
ٍ