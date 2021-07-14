from bs4 import BeautifulSoup
from requests import get
import re   
import html5lib
from yaml   import dump

#--------------- scraping the site----------------------------------

response = get('https://www.w3schools.io/file/yaml-sample-example/')
soup = BeautifulSoup(response.text, "html5lib")
title = soup.find('title').text
print(f'Titulo da página: {title}\n')
content = soup.find("pre")
exemplo_yml= content.text

#--------------- creating .txt file with scraped data.

exemplo_txt= open("exemplo.txt", "w")
exemplo_txt.write(exemplo_yml)
exemplo_txt.close()

#--------------- iterating the txt file to filter out the comments, \n and ''(null strings).

lista_linhas_yml=[]
exemplo_txt = open("exemplo.txt", 'r')
for linha in exemplo_txt:
    if '#'in linha:
        line = re.sub(r'#.*$', '', linha)
        lista_linhas_yml.append(line)
    else:
        lista_linhas_yml.append(linha)
exemplo_txt.close()

nova_yml=[]
for i in lista_linhas_yml:
    nova_yml.append(i.strip())

while '' in nova_yml:
    nova_yml.remove('')

#------------------ creating .yml file
with open ("new_yml.yml","w") as file:
    dump(nova_yml,file)
