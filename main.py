from bs4 import BeautifulSoup
import requests

url = input("Enter the URL of the USCCB website with the readings:")

html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')

divs = soup.find_all('div', class_ = 'content-body')

for div in divs:
    readings = div.text
    print(readings)