from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://bible.usccb.org/bible/readings/010823.cfm').text
soup = BeautifulSoup(html_text, 'lxml')

divs = soup.find_all('div', class_ = 'content-body')

for div in divs:
    readings = div.text
    print(readings)