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

4.Variables and data types 

name = "Alice"       # str
age = 25             # int
height = 5.6         # float
is_student = True    # bool

5.Control flow
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
6. functions python copy code
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

7. lists and dictionaries python
# List
fruits = ["apple", "banana", "cherry"]
print(fruits[0])

# Dictionary
person = {"name": "Bob", "age": 30}
print(person["name"])

8. Object-oriented programming python
class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, I'm {self.name}")

p1 = Person("Alice", 25)
p1.greet()

9. File handling python
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