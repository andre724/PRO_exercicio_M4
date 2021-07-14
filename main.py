from bs4 import BeautifulSoup
from requests import get
import re   
import html5lib

response = get('https://www.w3schools.io/file/yaml-sample-example/')
soup = BeautifulSoup(response.text, "html5lib")
title = soup.find('title').text
print(f'Titulo da página: {title}\n')
content = soup.find("pre")
exemplo_yml= content.text