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