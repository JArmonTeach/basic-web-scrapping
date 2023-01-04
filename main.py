from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://bible.usccb.org/bible/readings/010423.cfm').text
soup = BeautifulSoup(html_text, 'lxml')

for readings in soup.find_all(class_ = "content-body"):
    reading = readings.find_next_sibling().text
    print(reading)