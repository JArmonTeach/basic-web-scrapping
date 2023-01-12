from bs4 import BeautifulSoup
import requests
from pptx import Presentation

url = input("Enter the URL of the USCCB website with the readings:")

html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')

divs = soup.find_all('div', class_='content-body')

div_texts = [div.text for div in divs]

titles = ["First Reading", "Psalm", "Second Reading", "Alleluia Acclamation", "Gospel"]
for div_text, title in zip(div_texts, titles):
    print(title)
    print(div_text)



"Create PPT Presentation to add slides to"
ppt_slides = Presentation()

"Register the slide (Number refers to the layouts of each slide)"
slide1_register = ppt_slides.slide_layouts[1]



#saves in my local downloads folder
ppt_slides.save("C:/Users/Colorado/Downloads/Day_Readings.pptx")