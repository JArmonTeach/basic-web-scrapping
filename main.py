from bs4 import BeautifulSoup
import requests
from pptx import Presentation
from pptx.util import Inches, Pt

url = input("Enter the URL of the USCCB website with the readings:")

html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')

divs = soup.find_all('div', class_='content-body')

div_texts = [div.text for div in divs]

titles = ["First Reading", "Psalm", "Second Reading", "Alleluia Acclamation", "Gospel"]
for div_text, title in zip(div_texts, titles):
    print(title)
    print(div_text)



#Create PPT Presentation to add slides to
ppt_slides = Presentation()

#Adjust Slide size to be widescreen 16:9
ppt_slides.slide_width = Inches(16)
ppt_slides.slide_height = Inches(9)

#Register the slide (Number refers to the layouts of each slide; 6 is a blank slide)
slide1_register = ppt_slides.slide_layouts[6]

#Attach slide obj to slide
slide = ppt_slides.slides.add_slide(slide1_register)

#Adjust margins TODO: correct sizes
height = Inches(5.92)
width = Inches(10.01)
top = bottom = Inches(1)
left = right = Inches(1)

#Create textbox
txBox = slide.shapes.add_textbox(left, top, width, height)

#Create textframes
tf = txBox.text_frame

#create paragraph
p = tf.add_paragraph()
p.text = "TODO"
p.font.size = Pt(36)
p.font.name = 'Georgia'

#saves in local downloads folder
ppt_slides.save("C:/Users/Colorado/Downloads/Day_Readings.pptx")