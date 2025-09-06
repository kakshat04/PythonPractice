"""
re - search, findall, sub, split, match
"""

import re
"""
 Warmup
"""
# txt = "The Srain in Spain"
# value = re.search(r"^The.*Spain\Z", txt)
# print(value.group(0))
#
# value = re.findall(r"\s", txt)
# print(len(value))
# print(value.count(" "))
#
# value1 = re.findall(r"Portun", txt)
# print(value1)
#
# value2 = re.split(r"in",txt, 1)
# print(value2)
#
# value3 = re.sub(r"in", "by", txt)
# print(value3)
#
# value4 = re.search(r"\bS\w+", txt)
# print(value4.group())
#
# value5 = re.findall(r"\bS\w+", txt)
# print(value5)


# Validate Email
emails = ["alice@mail.com", "bad@@mail", "bob.smith@sub.example.co.uk"]
valid_emails = re.compile(r"^[a-zA-Z0-9._]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+$")
print([email for email in emails if valid_emails.match(email)])

# Validate ipv4 address
ips = ["10.0.0.1", "256.1.2.3", "192.168.1.100", "01.02.03.004"]
exp = r"(25[0-5]|2[0-4]\d|1?\d?\d)"
valid_ips = re.compile(rf"^{exp}\.{exp}\.{exp}\.{exp}$")
print(ip for ip in ips if valid_ips.match(ip))

# Extract domains from email list
text = "Team: a@x.com, b@dept.org, carol@sub.company.co"
domains = re.findall(r"\b@[a-zA-Z0-9._-]+\.[a-zA-Z]{2,}", text)
print(domains)

# Find all hashtags in a tweet
tweet = "Learning C# & #Python and #regex at #WHU! #100DaysOfCode"
all_hastags = re.findall(r"#\w+", tweet)
print(all_hastags)

# Normalize whitespace (collapse to single spaces)
s = "This   has\ttoo   many   spaces.\nAnd  newlines."
print(re.sub(r"\s+", " ", s))

# Split words by non-alphabetic characters
s = "Split-this_text,please!! Into words42 but ignore digits."
print(re.split(r"[^a-zA-Z]+", s))

#Extract dates (DD/MM/YYYY or YYYY-MM-DD)
s = "Two dates: 23/08/2025 and 2024-12-31, plus 99/99/9999 (bad)."
ddmmyy_exp = r"(?:0[1-9]|[12]\d|3[01])/(?:0[1-9]|1[0-2])/(?:19|20)\d{2}"
yymmdd_exp = r"(?:19|20)\d{2}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01])"
print(re.findall(rf"{ddmmyy_exp}|{yymmdd_exp}", s))

# Detect duplicate consecutive words (backreference)
s = "This is is a test. That that was odd."
dups = re.findall(r"\b(\w+)\s+\1\b", s, re.IGNORECASE)
print(dups)

# Extract quoted strings (non-greedy)
s = 'Say "hello world" and then "goodbye". Ignore "quotes \"inside\"" partially.'
print(re.findall(r'"(.*?)"', s))

# Extract numbers (integers & floats, with negatives)
s = "Profit: -12.5, cost: 100, delta: +0.75, noise: -.5"
# ['-12.5', '100', '+0.75', '-.5']  # note: '-.5' captured without leading 0
print(re.findall(r'[-+]?\.?\d+\.?\d{0,2}', s))

# Words starting with a capital letter (proper nouns)
s = "Alice met Bob in New York with dr. Watson."
# ['Alice', 'Bob', 'New', 'York', 'Watson']
print(re.findall(r'[A-Z]\w+', s))

# Remove simple HTML tags (quick-and-dirty)
html = "<p>Hello <b>world</b> & welcome!</p>"
# Hello world & welcome!
print(re.sub(r'<.*?>', '', html))

# Extract key=value pairs (quoted or bare)
s = 'user=alice id=42 role="admin user" active=true'
# {'user': 'alice', 'id': '42', 'role': 'admin user', 'active': 'true'}
kv_pair = re.findall(r'(\w+="?\s?\w+"?)+', s)
print(kv_pair)
dict1 = {}
for pair in kv_pair:
    k, v = pair.split("=")
    dict1[k] = v
print(dict1)


# kv = {k: v for k, v in (s.split('=') for s in kv_pair if '=' in s)}
# print(kv)

# Multiline: match lines that start with ERROR
log = """INFO: start
ERROR: failed to connect
WARN: retrying
ERROR: timeout"""

# ['ERROR: failed to connect', 'ERROR: timeout']
print(re.findall(r'^ERROR.*', log, re.MULTILINE))

# Mask credit card numbers except last 4
# Cards: **** **** **** 1234, **** **** **** 5678
s = "Cards: 4111 1111 1111 1234, 5500-0000-0000-5678"
print(re.sub(r'\b(\d{4})[- ]?(\d{4})[- ]?(\d{4})[- ]?(\d{4})\b', r'**** **** **** \4',s))




