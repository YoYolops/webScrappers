import re

a = 'asdas \n asd'

a = re.sub(r'\n', 'ZZZ', a)

print(a)