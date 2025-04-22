# try:
#     print(5/0)
# except ZeroDivisionError:
#     print('This is ZeroDivisionError')
# else:
#     print('this is normal division')
# finally:
#     print('whatever is execute')

# print('Please give me two numbers, I\'ll divide them:')
# print('Enter \'q to quite.')
# while True:
#     first_name=input('Please input first num:')
#     if first_name=='q':
#         break
#     second_name=input('Please input second num:')
#     if second_name=='q':
#         break
#     try:
#         answer=int(first_name)/int(second_name)
#     except ZeroDivisionError:
#         print('This is division by zero')
#     else:
#         print(answer)
from pathlib import Path
import os
dir = Path(__file__).resolve().parent
print(dir)
path = Path(f'{dir}/08-wirte.txt')
print(path)
try:
    contents=path.read_text(encoding='utf-8')
    print(contents)
except FileNotFoundError:
    print(f'This file {path} is not found!')
else:
    words=contents.split()
    print(words)
    num_words=len(words)
    print(f'This file has {num_words} words!')