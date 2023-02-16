import PyPDF2 , os
newdir = f'{os.getcwd()}\PdfFiles'
os.chdir(newdir)
def mergepdf(pdf_file,output_file):
    merge = PyPDF2.PdfMerger()
    for pdf in pdf_file:
        with open(pdf,'rb') as f:
            merge.append(f)
            print(f)

    with open(output_file,'wb') as f:
        merge.write(f)


if __name__ == '__main__':
    pdf_files = os.listdir()
    mergepdf(pdf_files,'merged_pdf.pdf')