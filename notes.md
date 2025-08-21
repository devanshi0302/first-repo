# Python Notes

## 1. Introduction to Python
- Python is a high-level, interpreted, and dynamically-typed programming language.
- Created by Guido van Rossum and first released in 1991.
- Emphasizes code readability with its clear syntax and indentation.

## 2. Key Features
- Easy to learn and use
- Interpreted language
- Dynamically typed
- Large standard library
- Cross-platform
- Supports multiple paradigms (procedural, OOP, functional)

## 3. Hello World Example
```python
print("Hello, World!")

name = "Alice"       # str
age = 25             # int
height = 5.6         # float
is_student = True    # bool

if age >= 18:
    print("Adult")
else:
    print("Minor")

# For loop
for i in range(5):
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# List
fruits = ["apple", "banana", "cherry"]
print(fruits[0])

# Dictionary
person = {"name": "Bob", "age": 30}
print(person["name"])

class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, I'm {self.name}")

p1 = Person("Alice", 25)
p1.greet()

# Write to a file
with open("file.txt", "w") as f:
    f.write("Hello, file!")

# Read from a file
with open("file.txt", "r") as f:
    content = f.read()
    print(content)

10. Useful Modules
math: mathematical functions
datetime: date and time operations
os: interacting with the operating system
sys: access to system-specific parameters
random: generate random numbers