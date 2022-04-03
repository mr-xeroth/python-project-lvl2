import json
from gendiff import generate_diff

dict1 = json.load(open('../../file1.json'))
dict2 = json.load(open('../../file2.json'))

diff = generate_diff(dict1, dict2)
print(diff)
