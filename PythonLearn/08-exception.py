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

# use multi files
def count_words(path_cwd):
    path = Path(path_cwd)
    # print(path)
    try:
        contents=path.read_text(encoding='utf-8')
        # print(contents)
        # caculate the word nums
        count_the=contents.lower().count('th')
        print(f'The count is {count_the}')
    except FileNotFoundError:
        return (f'This file {path} is not found!')
    else:
        words=contents.split()
        # print(words)
        num_words=len(words)

        return (f'This file has {num_words} words!')


path_cwds=[f'{dir}/08-wirte.txt',f'{dir}/08-file&exception.txt',f'{dir}/07-class.txt']
for path_cwd in path_cwds:
    answer=count_words(path_cwd)
    print(f'The answer is: {answer}')

# print('Please input two nums, calculate the sum')
# print('Enter "q" to exit')
# while True:
#     add1=input('Please input num1: ')
#     if add1=='q':
#         break
#     add2=input('Please input num2: ')
#     if add2=='q':
#         break
#     try:
#         sum=int(add1)+int(add2)
#     except ValueError:
#         print(ValueError)
#         pass
#     else:
#         print(f'The sum is {sum}')
    



