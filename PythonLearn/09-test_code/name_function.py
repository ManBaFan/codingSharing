def get_formated_name(first, last, middle=''):
    """general normally formate name"""
    if middle:
        full_name = f'{first} {middle} {last}'
    else:
        full_name = f'{first} {last}'
    return full_name.title()
# print(get_formated_name('ethan','fan'))
