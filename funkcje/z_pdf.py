import PyPDF2

pdfFileObj = open('sample.pdf', 'rb')

pdfReader = PyPDF2.PdfReader(pdfFileObj)

print(len(pdfReader.pages))

pageObj = pdfReader.pages[0]

strona = pageObj.extract_text()

with open('strona.txt', 'w', encoding='utf-8') as f:
    f.write(strona)

# plik_pdf = "drylab.pdf"
# pdf = PyPDF2.PdfReader(open(plik_pdf, "rb"))
#
# for strona_num in range(len(pdf.pages)):
#     strona = pdf.pages[strona_num]
#     obrazy = strona['/Resources']['/XObject'].get_object()
#     for obraz in obrazy:
#         if obrazy[obraz]['/Subtype'] == '/Image':
#             with open('obrazy.png', 'wb') as f:
#                 f.write(obraz)

from pdf2image import convert_from_path

plik = 'drylab.pdf'
obrazy = convert_from_path(plik)
for i, obraz in enumerate(obrazy):
    obraz.save(f'strona_{i}.png', 'PNG')
