# Este bot coleta dados do crescimento populacional da paraíba 
# entre 1872 e 2010

import requests
from bs4 import BeautifulSoup

page = requests.get("https://pt.wikipedia.org/wiki/Para%C3%ADba")

soup = BeautifulSoup(page.text, 'html.parser')

table = soup.select('.toccolours tbody tr')

excluir = [0,0,12,12]
for i in excluir:
    table.pop(i)

for elemento in table:
    ano = elemento.td.b.a.text
    populacao = elemento.next_element.next_element.next_element.next_element.next_element.text
    print(f'Ano: {ano}')
    print(f'População: {populacao}')
    print('-'*30)

