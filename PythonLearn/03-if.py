# 比较运算符，> < = and or in ;not in
catName = 'dave'
print('is the cat name dave?')
print(catName == 'dave')

print('is the cat name lisa?')
print(catName == 'lisa')

print('is the cat name daVe?')
print(catName == 'daVe'.lower())

print('lisa' == 'lisa' and 'dave' == 'dive')
print('lisa' == 'lisa' or 'dave' == 'dive')

cats = ['dave','lisa','candy']
if 'dave' in cats:
    print('dave in cats')
elif 'david' not in cats:
    print('david not in cats')
else:
    print('david is who')

# if ^ else
# alien_color = 'yellow'
alien_color = 'green'
# alien_color = 'red'
if alien_color == 'green':
    print('the player get 5 points!')

# if ^ else
# alien_color = 'yellow'
# alien_color = 'green'
alien_color = 'red'
if alien_color == 'green':
    print('the player get 5 points!')
else:
    print('the player get 10 points!')

alien_color = 'yellow'
# alien_color = 'green'
# alien_color = 'red'
if alien_color == 'green':
    print('the player get 5 points!')
elif alien_color == 'yellow':
    print('the player get 10 points!')
elif alien_color == 'red':
    print('the player get 15 points!')

age = 28
if age < 2:
    print('this is a baby')
elif 2<= age <4:
    print('this is a baby child')
elif 4<= age <13:
    print('this is a child')
elif 13<= age <18:
    print('the man is a teenager')
elif 18<= age <65:
    print('the man is an old teenager')
elif age >=65:
    print('the man is an old man')

# multiple conditions
favorite_fruits = ['apple','banana','tomato','orange','peach']
if 'apple' in favorite_fruits:
    print('You really like apple!')
if 'banana' in favorite_fruits:
    print('You really like banana!')
if 'tomato' in favorite_fruits:
    print('You really like tomato!')
if 'orange' in favorite_fruits:
    print('You really like orange!')
if 'peach' in favorite_fruits:
    print('You really like peach!')

# if 
# users = []
users = ['admin','guides','ethan','dave','lisa']
if users:
    for user in users:
        if user != 'admin':
            print(f'Hello {user}, thank you for logging in again.')
        elif user == 'admin':
            print(f'Hello {user},  would you like to see a status report?')
else:
    print('we need find some users.')

# current_users
current_users = ['admin','guides','ethan','dave','Lisa']
new_users = ['cindy','tiny','guides','lisa']
n_users_low = []
for n_user in new_users:
    for c_user in current_users:
        if n_user.lower() != c_user.lower():
            use_flag = False
        else:
            use_flag = True
            break
    if use_flag:
        print(f'{n_user} has used,please input new name!')
    else:
        print(f'the user name {n_user} is not used!')

# current_users 2
current_users = ['admin','guides','ethan','Dave','Lisa']
new_users = ['cindy','tiny','guides','lisa']
c_users_low = []
for c_user in current_users:
    c_users_low.append(c_user.lower())
print(c_users_low)
for n_user in new_users:
    if n_user.lower() in c_users_low:
        print(f'{n_user} has used,please input new name!')
    else:
        print(f'the user name {n_user} is not used!')
# for n_user in new_users:
#     use_flag = False
#     for c_user in current_users:
#         if n_user.lower() == c_user.lower():
#             use_flag = True
#             break
#     if use_flag:
#         print(f'{n_user} has used,please input new name!')
#     else:
#         print(f'the user name {n_user} is not used!')