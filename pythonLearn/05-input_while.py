# # rent veichle
# msg = input('Hello,what type of car do you want to rent? ')
# print(f'Let me see if I can find you a {msg}')

# # restaurant customer
# msg_res = input('Hello,how many persons have restaurant customer: ')
# in_res = int(msg_res)
# if(in_res >= 8):
#     print('Sorry, that isn\'t table!')
# else:
#     print('OK, that is table.')

# % 
# msg_di = input('Enter a number, and I\'ll tell you if it\'s 10: ')
# in_msg_di = int(msg_di)
# if in_msg_di%10 == 0 :
#     print(f'the num {in_msg_di} is 10x')
# else:
#     print(f'the num {in_msg_di} is not 10x')


# while loop & input & flag & break & continue
# promt = 'please input a series of pizza materias'
# promt += "\n(Enter 'quit' when you are finished.) "
# active = True
# while active:
#     msg = input(promt) 
#     if msg != 'quit':
#         print(msg)
#     else:
#         active = False

# break
# promt = 'please input a series of pizza materias'
# promt += "\n(Enter 'quit' when you are finished.) "
# while True:
#     msg = input(promt) 
#     if msg != 'quit':
#         print(msg)
#     else:
#         break
current_num = 0
while current_num < 10:
    current_num += 1
    if current_num%2 == 0:
        continue
    print(current_num)