import re

strng = "cats are smarter than Dogs"
z = re.match(r"[A-Z]ats", strng, re.IGNORECASE)
print(z.start())
print(z.end())
print(z.group())


strng = "Dogs are smarter than Cats"
y = re.search(r"[A-Z]ats", strng)
print(y.start())
print(y.end())
print(y.group())

strng = "Dogs are smater than Cats"
x = re.finditer(r"at", strng)
for data in x:
    print(data.group(), data.start(), data.end())

phone = "2004-959-559 # This is Phone Number"
w = re.search(r"\d*-\d*-\d*\s#", phone)
print(w.group())

v = re.search(r"#\s\w", phone)
print(v.group())

text = "He was carefully disguised but captured quickly by police."
print(re.findall(r"\w*ly", text))
print(re.findall(r'\b[aeiouAEIOU]\w*', text))

text1 = "cat caterpillar scat concatenat catwalk"
print(re.findall(r"\bcat\w*", text1))
print(re.findall(r'\Bcat\w*', text1))

# 1. Extract all email addresses from a string
text = "Contact us at support@example.com, hr@company.org, or info@domain.co.uk"
print(re.findall(r"[a-zA-Z0-9]+@[a-zA-Z0-9.]+\.[a-zA-Z]{2,}", text))

# 2. Validate a phone number (10-digit)
phone = "My number is 9876543210 and my friend's is 1234567890"
print(re.findall(r"\b\d{10}", phone))

# 3. Check if a string is a valid IPv4 address
ip = "192.168.1.1"
print(re.match(r"\d{0,3}\.\d{0,3}\.\d{0,3}\.\d{0,3}", ip))

random_string = "01010000010010101"
print(re.findall(r"(01)", random_string))

# 4. Split a sentence into words using regex

sentence = "Hello, how :are you doing today?"
print(re.findall(r"\b\w+\b", sentence))
print(re.split(r"[,:]", sentence))

# 6. Extract all hashtags from a tweet
tweet = "Loving #Python and #AI! #100DaysOfCode is awesome."
print(re.findall(r"#\w*", tweet))

# 7. Find all words starting with a capital letter
text = "Alice went to New York to vIsit Uncle John."
print(re.findall(r"\b[A-Z]\w*", text))

# 8. Mask all digits of a credit card except the last 4
cc = "Card: 1234-5678-9012-3456"
masked = re.sub(r'\d', 'X', cc)
print(masked)

# 9. Extract file names with .jpg or .png extension
files = "img1.jpg img2.png doc1.pdf photo.jpeg img3.JPG"
print(re.findall(r'\w+\.(?:jpg|png)\b', files))

# 10. Replace all whitespace (spaces, tabs, newlines) with a single space
messy = "This\tis a  messy\nstring with  \t irregular   spaces"
print(re.sub(r'\s+', ' ', messy).strip())




