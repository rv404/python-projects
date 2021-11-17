import requests
from bs4 import BeautifulSoup

html = requests.get('http://www.pygame.org/docs/')
scr = html.content
soup = BeautifulSoup(scr, 'lxml')
html = soup.prettify()
with open('pygame.html', 'w') as f:
    f.write(html)