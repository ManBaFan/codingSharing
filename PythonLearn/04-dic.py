# first_name、last_name、age 和 city
per_dic = {}
print(per_dic)

# add
per_dic['first_name'] = 'fan'
per_dic['last_name'] = 'lixin'
per_dic['age'] = '32'
per_dic['city'] = 'hangZhou'
print(per_dic)

# select
print(per_dic['first_name']+" & "+ per_dic['last_name'])
# get(arg1,arg2)
print(per_dic.get('first_nam','No the man'))
# get(arg1)
print(per_dic.get('first_nam'))

# update
print(f'orign dic is {per_dic}')
per_dic['first_name'] = 'Fan'
per_dic['last_name'] = 'liXin'
print(f'after dic is {per_dic}')

# delete
del per_dic['last_name']
print(f'after del of dic is {per_dic}')

# item
for key,value in per_dic.items():
    print(f'\nKey:{key}')
    print(f'Value:{value}')

# item key
for key in per_dic:
    print(key.title())
# or
for key in per_dic.keys():
    print(key.upper())

# item value
for value in per_dic.values():
    print(value.lower())

print(list(range(30)))
print(set(range(30)))


# list embed dict
alion1 = {1:1,2:2}
alion2 = {21:21,22:22}
list_dict = [alion1,alion2]
# print(list_dict)
for alion in list_dict:
    print(f"the dict is {alion}")

# dict embed alion
alion3 = {
    'ethan':['c','python','go'],
    'dave':['c'],
    'kobe':['ruby','c++']
}
for alion in alion3.keys():
    print(f'{alion} favirote language is:')
    for la in alion3[alion]:
        print(f'\t{la}')

# dict embed dict, inner dict item type is same
alion4 = {
    'ethan':{'age':32,'gender':'male','height':172},
    'dave':{'age':42,'gender':'female','height':170}
}

for user,user_info in alion4.items():
    print(f'This is {user.title()} information:')
    print(f'\tthe age is {user_info['age']}\n\tthe gender is {user_info['gender'].title()}\n\tthe height is {user_info['height']}')

# for i in alion4:
#     print(f'This is {i.title()} information: ')
#     print(f'\tthe age is {alion4[i].get('age')}')
#     print(f'\tthe gender is {alion4[i].get('gender').title()}')
#     print(f'\tthe height is {alion4[i].get('height')}')