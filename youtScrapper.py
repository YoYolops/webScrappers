import requests
from bs4 import BeautifulSoup
import re

page = requests.get('https://pt.wikipedia.org/wiki/Lista_dos_canais_com_mais_inscritos_do_YouTube')

soup = BeautifulSoup(page.content, 'html.parser')

# A linha seguinte encontra a Tabela desejada e salva em table:
table = soup.body.find('div', id = 'content').find('div', id = 'bodyContent').find('div', id = 'mw-content-text').find('div', class_ = 'mw-parser-output').find('table', class_ = "wikitable sortable")

tableRows = table.find_all('tr') # Retorna uma lista com as informações das linhas da tabela

linhas = []

# O laço a seguir cria uma lista de listas, a listas filhas armazenam os dados das linhas da tabela
cont = 0
for line in tableRows:
    if cont == 0: # Verifica se o loop está rodando pela primeira vez, pois o primeiro item 'line' foge ao padrão e deve ser tratado diferente
        temporaria = []

        for th in line.find_all('th'): # Encontro todas as tags <th>, pois são as que têm a informação desejada
            temporaria.append(re.sub(r'\[.*\]|\n', '', th.text)) # Com a tag em mãos, extraio o seu texto e retiro caracteres indesejados com REGEX e o salvo na lista temporária

        linhas.append(temporaria) 
        cont += 1 # Adiciona um à variável de controle, pois o bloco 'if' não deve mais ser executado
    else: # Da segunda linha em diante, faço o mesmo passo que o do bloco de cima, exceto que agora lido com tags <td> e não <th>
        temporaria = []

        for td in line.find_all('td'):
            temporaria.append(re.sub(r'\[.*\]|\n', '', td.text))

        linhas.append(temporaria)

linhas.pop() # Retira a última lista, que é vazia

for i in linhas: 
    print(i)
    print()



    

