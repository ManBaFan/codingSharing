from pathlib import Path
import json

dir=Path(__file__).resolve().parent
def json_dump(path_cwd,numbers):
    path = Path(path_cwd)
    contents=json.dumps(numbers)
    path.write_text(contents)
    return path.read_text()

def json_load(path_cwd):
    path = Path(path_cwd)
    if path.exists():
        contents=path.read_text()
        json_contents=json.loads(contents)
        # print(contents)
        print(json_contents)
        # for key,value in json_contents.items():
        #     print(value)
        #     print(key)
    else:
        user_name=input('Please input your name: ')
        json_dump(path_cwd,user_name)
# dump json contents
path_cwd=f'{dir}/08-test.json'
# numbers = [1,2,3,4,5,6,'fsdfs333']
# result=json_dump(path_cwd,numbers)
# print(result)

# load json contents
json_load(path_cwd)

with open(path_cwd,'r',encoding='utf-8') as f:
    print(f"This is {json.loads(f.read())}")