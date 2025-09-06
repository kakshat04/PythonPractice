def fizzbuzz(n: int) -> list[str]:
    l = []
    for i in range(1, n + 1):
        if i%3 == 0 and i%5 == 0:
            l.append("FizzBuzz")
        elif i % 3 == 0:
            l.append("Fizz")
        elif i % 5 == 0:
            l.append("Buzz")
        else:
            l.append(str(i))
    return l


import  re
def is_palindrome(s: str) -> bool:
    s1 = re.sub(r"[^A-Za-z0-9]", "", s)
    print(s1.lower())
    print(s1[::-1].lower())
    if s1.lower() == s1[::-1].lower():
        return True
    else:
        return False
print(is_palindrome("A man, a plan, a canal: Panama"))

def are_anagrams(a: str, b: str) -> bool:
    # TODO: implement
    return sorted(a) == sorted(b)
print(are_anagrams("hello","world"))

def remove_dups(lst):
    new_lst = []
    for i in lst:
        if i in new_lst:
            continue
        else:
            new_lst.append(i)
    return new_lst

print(remove_dups([1,3,4,2,2,1]))

items = [1, 2, 2, 3, 1, 4, 3]
out = list(dict.fromkeys(items))
print(out)

dict1 = {1: "A", 2: "B", 3: "C", 4: "D"}
print(list(dict1.keys()))

x = {1}
print(type(x))

def first_last(tup:tuple) -> int:
    return tup[0], tup[-1]
# You may write helper functions and tests below.
print(first_last((1,2,3)) == (1,3))

a = [[1], [2], [1], [2], [3]]
b = []
for i in a:
    b.extend(i)
print(b)

t = ((1, 2), (3, 4), (5,))
l = []


for a in t:
    for b in a:
        l.append(b)
print(tuple(l))
