# rent veichle
msg = input('Hello,what type of car do you want to rent? ')
print(f'Let me see if I can find you a {msg}')

# restaurant customer
msg_res = input('Hello,how many persons have restaurant customer: ')
in_res = int(msg_res)
if(in_res >= 8):
    print('Sorry, that isn\'t table!')
else:
    print('OK, that is table.')

msg_di = input('Enter a number, and I\'ll tell you if it\'s 10: ')
in_msg_di = int(msg_di)
if in_msg_di%10 == 0 :
    print(f'the num {in_msg_di} is 10x')
else:
    print(f'the num {in_msg_di} is not 10x')


# while loop & input & flag & break & continue
promt = 'please input a series of pizza materias'
promt += "\n(Enter 'quit' when you are finished.) "
active = True
while active:
    msg = input(promt) 
    if msg != 'quit':
        print(msg)
    else:
        active = False

# break
promt = 'please input a series of pizza materias'
promt += "\n(Enter 'quit' when you are finished.) "
while True:
    msg = input(promt) 
    if msg != 'quit':
        print(msg)
    else:
        break
# flag
current_num = 0
while current_num < 10:
    current_num += 1
    if current_num%2 == 0:
        continue
    print(current_num)

# move elements between lists
no_ver_users = ['kobe', 'stephen', 'lebron']
ver_users = []
while no_ver_users:
    no_ver_user = no_ver_users.pop()
    print(f'no vertifite name is {no_ver_user}')
    ver_users.append(no_ver_user)

print('The follow name has been confirmed:')
for name in ver_users:
    print(name)

# delete especial value in list
animals = ['dog', 'cat', 'lion', 'cat', 'tiger']
print(animals)

while 'cat' in animals:
    animals.remove('cat')
print('The zoo have below animals: ')
for animal in animals:
    print(f'\t{animal}')

# fill  dictionary by input
responses = { }
polling_activity = True

while polling_activity:
    name = input("\nwhat's your name? ")
    response = input("\nwhat\'s your favirote moutain? ")
    responses[name] = response
    repeat = input("\nWould you like to let another person respond? (Yes/No)")
    if repeat.title() == 'No':
        polling_activity = False

# indicate result
print('The result is')
for names, moutain in responses.items():
    print(f"\t{names} would like to climb {moutain}.")