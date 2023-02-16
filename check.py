import os
os.chdir(f'{os.getcwd()}\PdfFiles')
with open('merged_pdf.pdf','rb') as f:
    # f.write('Hii')
    print(f.read())