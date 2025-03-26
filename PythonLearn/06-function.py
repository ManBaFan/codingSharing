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


def greet_user2(username,sex):
    print(f"Hello, {username} is {sex}!")

greet_user2("Lixin","male")


# 位置形参，关键字形参，默认形参，可变参数
def greet_user3(firstname,lastname,middlename=None):
    if middlename:
        fullname = f"{firstname} {middlename} {lastname}"
    else:
        fullname = f"{firstname} {lastname}"
    print(f"Hello, name is {fullname}!")

greet_user3("Ethan","Bryant")

# 返回值，字符串，数字，列表，字典
def greet_user4(firstname,lastname,middlename=None):
    if middlename:
        fullname = f"{firstname} {middlename} {lastname}"
    else:
        fullname = f"{firstname} {lastname}"
    return fullname

getfullname = greet_user4("Ethan","Bryant")
print(f"Hello, name is {getfullname}!")

# 返回值是字典
def get_user5(firstname,lastname,middlename=None):
    user={'first':firstname,'last':lastname}
    if middlename:
        user['middle']=middlename
    return user

user_info = get_user5('Ethan','Bryant','Fan')
print(user_info)

# function is combined with while loop
def get_user5(firstname,lastname,middlename=None):
    user={'first':firstname,'last':lastname}
    if middlename:
        user['middle']=middlename
    return user

while True:
    print('please input your Firstname:')
    print("enter 'q ' at anytime to quit")
    n_f = input('First name: ')
    if n_f == 'q':
        print('it\'s over!')
        break
    n_l = input('Last name: ')
    if n_l.lower() == 'q':
        print('it\'s over!')
        break
    user_info = get_user5(n_f,n_l)
    print(f'user name info is {user_info}')

# function's paragram is list
def print_model(unprint_list,complete_list):
    """print item"""
    print_item = unprint_list.pop()
    print(f"The print item is {print_item}")
    complete_list.append(print_item)

def show_print_model(complete_list):
    """show prinit item"""
    for item in complete_list:
        print(f'The complete print item is {item}')

unprint_list = ['dave','lisa','daria',2]
complete_list = []
print_model(unprint_list,complete_list)
show_print_model(complete_list)
