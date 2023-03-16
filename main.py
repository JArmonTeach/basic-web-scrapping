from bs4 import BeautifulSoup
import requests
from pptx import Presentation
from pptx.util import Inches, Pt

# Send a GET request to the website and parse the HTML content
url = input("Enter the URL of the USCCB website with the readings:")
html_text = requests.get(url)
soup = BeautifulSoup(html_text.content, 'html.parser')

# Locate the HTML elements that contain the text you want to scrape
text = soup.find(class_='content-body').get_text()

# Split the text into paragraphs based on <br> tags
paragraphs = text.split('<br>')

# Create a new PowerPoint presentation, set the size of the slide and add the first slide
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
textbox.text = paragraphs[0].strip()
font = textbox.text_frame.paragraphs[0].font

# Add the scraped text to slide(s)
line_count = 1
for paragraph in paragraphs[1:]:
    # Split each paragraph into lines based on newline characters
    lines = paragraph.split('\n')
    for line in lines:
        # Check if the text in the current slide has exceeded 13 lines
        if line_count >= 13:
            # Create a new slide and text box
            slide = prs.slides.add_slide(prs.slide_layouts[6])
            textbox = slide.shapes.add_textbox(left, top, width, height)
            font = textbox.text_frame.paragraphs[0].font
            line_count = 1
        # Add the line to the current slide's text box
        textbox.text_frame.add_paragraph().add_run(line.strip())
        line_count += 1

# Save the PowerPoint presentation
prs.save("C:/Users/Colorado/Downloads/Day_Readings.pptx")