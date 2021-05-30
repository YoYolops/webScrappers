from bs4 import BeautifulSoup
import json

html = open("spells.html", "r").read()
sopa = BeautifulSoup(html, 'html.parser')

divs = sopa.find_all('div', class_="grid-item spell-item")
spells = []

counter = 0
for div in divs:
    counter += 1
    print(f"coletando feitiço {counter}")

    nome = div.find('div', class_= "spell-body").find('div', class_="title").find('div', class_="name").p.text

    levelBrutus = div.find('div', class_="level").text
    level = ''
    for i in levelBrutus:
        if i.isdigit():
            level += i
        
    tipoBrutus = div.find('div', class_= "spell-body").find('div', class_="title").find('div', class_="name").find('p', class_="school").text
    tipo = ''
    for i in tipoBrutus:
        if not i.isdigit():
            tipo += i

    detailsDivList = div.find('div', class_= "spell-body").find('div', class_="details").find('div', class_="meta").find_all('div', class_="meta-item")
    detailsList = []
    for i in detailsDivList:
        detailsList.append(i.div.text)

    tempoConjuracao = detailsList[0]

    rangeBrutus = detailsList[1]
    range = ''
    for i in rangeBrutus:
        if i.isdigit():
            range += i
    if range == '':
        range = '0'

    duration = detailsList[3]

    descricaoList = div.find('div', class_= "spell-body").find('div', class_="details").find('div', class_="description").find_all('p')
    description = ''
    for i in descricaoList:
        description += str(i)

    spell = {
        "id": counter,
        "name": nome,
        "level": level,
        "type": tipo,
        "conjurationTime": tempoConjuracao,
        "range": range,
        "duration": duration,
        "description": description
    }

    spells.append(spell)
    print(spell)

finalJSON = {
    "spellsData": spells
}

with open("spells.json", "w", encoding='utf8') as outfile:
    json.dump(finalJSON, outfile, ensure_ascii=False)