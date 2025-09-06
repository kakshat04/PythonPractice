a = 10
print(type(a))


b = "Hello, World!"
print(b[-5:-2])  #orl
print(b[2:])
print(b[:5])
print(f"{b}, this is Akshat")
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
print(r"\nThis is 'Akshat' here")

txt = "banana"
x = txt.center(100)
y = txt.center(100, "O")
print(x)
print(y)

str1 = "Mississippi 12"
print(str1.rindex("i"))
print(str1.casefold())
print(str1.lower())
print(str1.lower().count("s"))
dict1 = {}
for i in str1:
    if dict1.get(i) is None and i.isalpha():
        dict1[i] = str1.count(i)
print(dict1)

for i in range(10, 1, -1):
    print(i)

thislist = ["apple", "banana", "cherry", "banana"]
print(thislist)
print(thislist.index("banana"))
print(max([i for i, v in enumerate(thislist) if v == "banana"]))
print(max(thislist))
thislist[1] = "mango"
print(thislist)
thislist.insert(1, "mango")
print(thislist)
thislist.extend(["sadsd", "dsd"])
print(thislist)
thislist.append("asdad")
print(thislist)
thislist.remove("mango")
print(thislist)
thislist.pop(-3)
print(thislist)

thislist.sort(reverse=True)
print(thislist)
thislist.reverse()
print(thislist)


from copy import copy, deepcopy

original = [1, 2]
new = copy(original)
new[0] = 99
print(original)

new1 = deepcopy(original)
new1[0] = 99
print(original)

import copy

original = [1, 2]
deep = copy.deepcopy(original)

deep[0] = 99
print(original)  # [[1, 2], [3, 4]] ← not affected

original = [1, 2]
shallow = copy.copy(original)

shallow[0] = 99
print(original)

tupl1 = tuple("1")
print(type(tupl1))

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(fruits)
print(green)
print(yellow)

l = {1,3,4,5,6}
l2 = {10,20,30,40,50}
l3 = l | l2
l4 = l.update(l2)
print("##")
print(l)
print(l3)
t = [2,4]
t.extend(l)

print(t)
l.remove(3)
print(l)
l.discard(6)
print(l)
l.pop()
print(l)
l.clear()




day = 2
match day:
    case 1:
        print("day")
    case 2:
        print("night")
    case _:
        print("something else")


month = 5
day = 6
match day:
    case 1|2|3|4|5 if month==5:
        print("weekday")
    case 6|7 if month==5:
        print("weekend")

for i in range(2,10,2):
    if i % 2 == 0:
        print(i)
        break
    else:
        print("no")
else:
    print("x")


subject = input("Subject: ")
score = int(input("Score: "))

match subject:
    case "Physics" | "Chemistry" if score >= 80:
        print("Good in Science")
    case "English" | "French" if score >= 80:
        print("Good in Language")
    case _:
        print("Need Improvement")

# deep copy
a = [1,2,3]
b = a[:]
b.append(4)
print(a)

import copy
a = [[1,2,3],[4,5,6]]
b = copy.copy(a)
b[0][0]=5
print(a)

a = [[1,2,3],[4,5,6]]
c = copy.deepcopy(a)
c[0][0]=10
print(a)

for i in range(10):
    print(i, end="*")

a = 0
b = 1
for i in range(1, 10):
    c = a + b
    a = b
    b = c
    print(b)