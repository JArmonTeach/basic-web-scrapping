from bs4 import BeautifulSoup
import requests
from pptx import Presentation
from pptx.util import Inches, Pt

# Send a GET requestto the website and parse the HTML content
url = input("Enter the URL of the USCCB website with the readings:")
html_text = requests.get(url)
soup = BeautifulSoup(html_text.content, 'html.parser')

# Locate the HTML elements that contain the text you want to scrape
# scraped_text = []
# max_chars_per_slide = 520
# for element in soup.find_all(class_='content-body'):
#     scraped_text.append(element.get_text())
text = ''
for element in soup.find_all(class_='content-body'):
    text += element.get_text()

# Join the elements of the list into a single string
# text = '\n'.join(scraped_text)

# Create a new PowerPoint presentation, set the size of the slide and add that new slide
prs = Presentation()
prs.slide_width = Inches(16)
prs.slide_height = Inches(9)
slide = prs.slides.add_slide(prs.slide_layouts[6])

# Create a text box on the slide
left = Inches(1)
top = Inches(.55)
width = Inches(14)
height = Inches(7.98)
textbox = slide.shapes.add_textbox(left, top, width, height)

# Reformat the text
font_name = 'Georgia'
font_size = Pt(36)
textbox.text = text
font = textbox.text_frame.paragraphs[0].font

# Add the scraped text to slide(s)
chars_written = 0
lines_written = 0
max_chars_per_line = 40
max_lines_per_slide = 13
for char in text:
    textbox.text += char
    chars_written += 1
    if chars_written % max_chars_per_line == 0:
        textbox.text += '\n'
    if char == '\n' or '<br>':
        lines_written += 1
        if lines_written >= max_lines_per_slide:
            slide = prs.slides.add_slide(prs.slide_layouts[6])
            left = Inches(1)
            top = Inches(.55)
            width = Inches(14)
            height = Inches(7.98)
            textbox = slide.shapes.add_textbox(left, top, width, height)
            font.name = 'Georgia'
            font.size = Pt(36)
            textbox.text = ''
            font = textbox.text_frame.paragraphs[0].font
            chars_written = 0
            lines_written = 0

# Save the PowerPoint presentation
prs.save("C:/Users/Colorado/Downloads/Day_Readings.pptx")