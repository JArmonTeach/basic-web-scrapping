# Web Scrapping App

## Project Description
This Python program web scrapes text and inserts it into PowerPoint slides. 

Python 3.8.5 was used so as to learn its basic syntax and semantics. This also allowed to learn how to web scrape with BeautifulSoup and how to automate a PowerPoint presentation using the pptx library.

A challenge that came about when formatting the scrapped text unto the PowerPoint slides. The solution of checking the original HTML formatting of the text, adjusting how to split the text based on the website's formatting and then looping through the process to create the slide, format the text and insert it into the slide will be helpful for future uses of scrapping data from a website. In other projects, it will help to understand how the text is organized and how to clean that data for better use.

## Installation
If using VSCode, install Python extension.

Install Python interpreter: 
    For windows: download from https://www.python.org/downloads/

    For macOS: will need to apackage management system like Homebrew, then install using Homebrew `brew install python3` in terminal prompt

    For Linux: can install Python3 but for other packages install `pip` with `get-pip.py`

Run Python code.

## Usage
    1. Paste the link from the USCCB readings website. (NOTE: the formatting of this program was intended to take text from this website and put them unto PowerPoint slides. If taking texts from other websites, then the class name and the formatting of the web scrapping needs to be changed.)
    2. The automatic download will appear in the local machine's Download folder named "Day_Readings.pptx"

## Credits
    Beautiful Soup Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    Python Pptx library Documentation: https://python-pptx.readthedocs.io/en/latest/

## License 
    MIT License

    Copyright (c) [2023] [JohnArmon Antolin]

    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.