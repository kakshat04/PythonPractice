"""
serialization is of 3 types:
1. pickle -- import pickle, rb/wb, .pkl
2. json -- import json
3. yaml -- import yaml
"""
import pickle

data1 = {'name': 'Alice', 'age': 30, 'city': 'New York'}

with open("data.pkl", "wb") as f:
    pickle.dump(data1, f)

with open("data.pkl", "rb") as f:
    z = pickle.load(f)
    print(z)


class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

person = Person('Alice', 30, 'New York')
with open("data1.pkl", "wb") as f:
    pickle.dump(person, f)