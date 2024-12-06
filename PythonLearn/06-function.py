# with open("data.txt", "w") as f:
#     f.write("Hello, World1!")

# with open("data.txt", "r") as f:
#     print(f.read())

# try:
#     x = 10 / 0
# except ZeroDivisionError as e:
#     print(f"Error: {e}")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old.")

p = Person("Lixin", 25)
p.greet()

def greet_user(username):
    print(f"Hello, {username}!")

greet_user("Lixin")