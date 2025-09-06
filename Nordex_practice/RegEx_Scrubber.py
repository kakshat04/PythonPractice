"""
Write a Python function that:

Removes IP addresses (e.g., 192.168.0.1) and email addresses (e.g., admin@nordex.com) from a given log string.

Replace them with [REDACTED].
"""

import re


log_string = "asdasd 192.168.0.1 adadad admin@nordex.com adad"
new_string = re.findall(r'\b(\d{1,3}\.){3}\d{1,3}\b', log_string)

print(new_string)

"""
Check if a string contains only alphabets
"""
log_string = "Hello12"
z = bool(re.fullmatch(r"[a-zA-Z]+", log_string))
print(z)

"""
Validate an email address
"""
email = "kumar-04@gmai.com"
z = bool(re.fullmatch(r"[\w\.-]+@[\w\.-]+\.\w+", email))
print(z)
