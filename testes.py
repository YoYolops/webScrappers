import re

a = 'camarada[133] e[1] \n'

a = re.sub(r'\[.*\]|\n', '', a)

print(a)