# Write a function to check if a string is a palindrome.
def palindrome(num):
    if num == num[::-1]:
        return True
    else:
        return False

x = palindrome("hannah")
print(x)

# Implement Fibonacci using recursion and memoization.
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))

def fibonacci2(n):
    a = 0
    b = 1
    if n == 2:
        print(n)
    else:
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
            print(b)
print(fibonacci2(10))

# Remove duplicates from a list while preserving order.
list1 = [1, 2, 2, 3, 1, 4]
print(list(set(list1)))

# Count the frequency of words in a string.
word = "TomDickHarryippi"
dictionary = {}
for letter in word:
    if dictionary.get(letter) is None:
        dictionary[letter] = 1
    else:
        dictionary[letter] += 1
print(dictionary)

# Reverse words in a sentence.
sentence = "Hello are you"
new_sentence = ""
for i in sentence.split():
    new_sentence += i[::-1] + " "
print(new_sentence)

# Validate if a string is a valid IPv4 address using regex.
ip = "192.158.225.17"
import re
print(re.match(r"^((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$", ip))



# Write a custom iterator class in Python.
class custom_iter:
    def __init__(self):
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < 5:
            self.count += 1
            return self.count
        else:
            raise StopIteration


custom_iter = custom_iter()
for i in custom_iter:
    print(i)

# Write a decorator that times the execution of a function

import time
def decorator(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print(f"Function '{function.__name__}' executed in {end - start} seconds.")
        return result
    return wrapper

@decorator
def check():
    time.sleep(2)
    print("yes")

check()