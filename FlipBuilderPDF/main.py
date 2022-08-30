import requests
from bs4 import BeautifulSoup
from PIL import Image
from convert import convert_pdf, merge_pdf
import os


def get_pages(base_url):
    i = 1
    while True:
        HTML_URL = f'files/basic-html/page{i}.html'
        r = requests.get(base_url+HTML_URL)
        soup = BeautifulSoup(r.text, 'html.parser')
        for e in soup.findAll('title'):
            title = e.get_text()
        if title == 'FlipBuilder Online Service Error':
            break
        i += 1
        
    return i
file = open('URLS.cfg', 'r')
url_number = 1
urls = [x.strip() for x in file.read().splitlines()]
        

for url in urls:
    BASE_URL = url
    PAGES = get_pages(BASE_URL)
    for i in range(1,PAGES):
        print(f'[URL #{url_number} is parsing. [{i}/{PAGES-1}]]')
        url = BASE_URL + f'files/mobile/{i}.jpg?211112143732'
        p = requests.get(url)
        out = open(f'temp/{i}.jpg', "wb")
        out.write(p.content)
        out.close()
        convert_pdf(i)
    merge_pdf(PAGES, url_number)
    for i in range(1,PAGES):
        os.remove(f'temp/{i}.jpg')
        os.remove(f'temp/{i}.pdf')
    url_number += 1
print('Parsing successfully completed!\n')
file.close()