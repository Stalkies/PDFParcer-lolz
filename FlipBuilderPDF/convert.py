from PIL import Image
from PyPDF2 import PdfMerger
import datetime
def convert_pdf(i):
    image_1 = Image.open(rf'temp/{i}.jpg')
    im_1 = image_1.convert('RGB')
    im_1.save(rf'temp/{i}.pdf')
def merge_pdf(pages, result):
    pdfs = [f'temp/{x}.pdf' for x in range(1,pages)]
    merger = PdfMerger()
    for pdf in pdfs:
        merger.append(pdf)
    merger.write(f'result-{result}.pdf')
    merger.close()