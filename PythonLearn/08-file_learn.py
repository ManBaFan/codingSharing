'''learn file input use and output'''
from pathlib import Path
import os
import re

# 当前工作目录
print("Current Working Directory:", os.getcwd())
# 脚本路径
print(f"脚本路径: {__file__}")
# 脚本所在目录
print("脚本所在目录:", Path(__file__).resolve().parent)
sdir = Path(__file__).resolve().parent
pa = Path(f'{sdir}/08-file&exception.txt')
contents = pa.read_text()
# print(contents)
lines = contents.splitlines()
# print(lines)
pi = ''
for i in lines:
    # pi+=i
    pi+=i
# print(f'after split: \n {pi.replace(' ','')}')
# remove empty 
pi_re = re.sub(r'\s+','',pi)
print(f'after split: \n {re.sub(r'\s+','',pi)}')
print(len(pi))
print(len(pi_re))
print(pi[:10])
print(pi_re[:10])
# birthday = input('Enter your birthday, format mmddyy: ')
# if birthday in pi_re:
#     print('That is obtain my birthday!')
# else:
#     print('Do not obtain!')

path_w = Path(f'{sdir}/08-wirte.txt')
path_w.write_text('123')
print(path_w.read_text())

# write muti line content
strs = 'This is python.\n'
strs += 'so what?\n'
strs += 'I can write high quality python.\n'
path_w.write_text(strs)
print(path_w.read_text())