# """
# 🔹 1. Log File Analyzer
# Problem:
# Write a Python script to parse a log file (system.log) and extract all lines that:
#
# Contain the word "ERROR"
#
# Have a timestamp in the format YYYY-MM-DD HH:MM:SS
#
# Sample Log Line:
# 2025-07-15 09:32:10 - ERROR - Turbine T34 voltage drop detected
#
# Expected Output:
# A list of such log lines with timestamp and error message.
# """
# import re
#
# def log_file_analyser(log_file):
#     with open(log_file, 'r') as f:
#         lines = f.readlines()
#         for line in lines:
#             if re.match(r"\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2} - ERROR - *", line):
#                 print(line)
#
# log_file_analyser("system.log")
#
#
# if __name__ == "__main__":
#     log_file = "system.log"
#     log_file_analyser(log_file)

ItemsInCart = 0


def add_to_cart(items_to_add):
    global ItemsInCart
    if items_to_add < 0:
        raise Exception("Cannot add a negative number of items.")
    if items_to_add > 5:
        raise Exception("Cart limit exceeded.")

    ItemsInCart += items_to_add
    print(f"{items_to_add} items added. Total in cart: {ItemsInCart}")
try:
    add_to_cart(2)  # Add 2 items
    add_to_cart(-1)  # This should raise an exception
except Exception as e:
    print(e)


person = ("Rahul", 25, 5.9)
print(f"Age: {person[1]}")
try:
    person[0] = "Akshat"
except:
    print("Tuple Modification failed, as tuple is immutable")

