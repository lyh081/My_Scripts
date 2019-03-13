import os
from PyPDF2 import PdfFileReader, PdfFileWriter
base = os.getcwd()


def Delete_Page(file_path, page_number):
    old_file = open(file_path, 'rb')
    pdf_input = PdfFileReader(old_file)
    if old_file in locals():
        old_file.close()
    pdf_ouput = PdfFileWriter()
    pdf_delete = PdfFileWriter()
    page_nums = pdf_inserted.numPages
    if page_number > page_nums:
        print('Delete Page number should between 0 to {}'.format(page_nums))
        return 0
    for i in range(page):
        if page_number == i:
            with open('Page{}.pdf', 'wb') as f:
                pdf_delete.write(f)
        else:
            pdf_ouput.addPage(pdf_input.getPage(i))

    with open(file_path, 'wb') as f:
        pdf_ouput.write(f)
    print('Delete Done!')

if __name__ == "__main__":
    file_path = base + 'test.pdf'
    Delete_Page(file_path, 1)
