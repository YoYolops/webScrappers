import requests
from bs4 import BeautifulSoup
import re

page = requests.get('https://pt.wikipedia.org/wiki/Lista_dos_canais_com_mais_inscritos_do_YouTube')

soup = BeautifulSoup(page.content, 'html.parser')

table = soup.body.find('div', id = 'content').find('div', id = 'bodyContent').find('div', id = 'mw-content-text').find('div', class_ = 'mw-parser-output').find('table', class_ = "wikitable sortable")
tableRows = table.find_all('tr')

linhas = []

cont = 0
for line in tableRows:
    if cont == 0:
        temporaria = []

        for th in line.find_all('th'):
            temporaria.append(re.sub(r'\n', '', th.text))

        linhas.append(temporaria)
        cont += 1
    else:
        temporaria = []

        for td in line.find_all('td'):
            temporaria.append(re.sub(r'\n', '', td.text))

        linhas.append(temporaria)

linhas.pop()

for i in linhas:
    print(i)
    print()



    

