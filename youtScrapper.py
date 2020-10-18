
import requests
from bs4 import BeautifulSoup

page = requests.get('https://pt.wikipedia.org/wiki/Lista_dos_canais_com_mais_inscritos_do_YouTube')

soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find('body').find('div', class_ = 'mw-body').find(id = 'bodyContent').find(id = 'mw-content-text').find('table', class_ = 'wikitable') # Existe mais de uma tag table com essa classe, ele seleciona a primeira

print(table)