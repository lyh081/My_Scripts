import os
from PyPDF2 import PdfFileReader, PdfFileMerger


def open_file(file_path):

    old_file = open(file_path, 'rb')
    pdf_input = PdfFileReader(old_file, strict=False)
    if old_file in locals():
        old_file.close()

    return pdf_input


def Insert(file1, file2, page_index, merged_name):

    pdf_inserted = open_file(file1)
    pdf_insert = open_file(file2)
    if not pdf_insert or not pdf_inserted:
        return 0
    page_nums = pdf_inserted.numPages
    if page_index < 0 or page_index > page_nums:
        print('Insert Position Error')
        print('Insert Page number should between 0 to {}。'.format(page_nums))
        return 0
    output = PdfFileMerger(False)
    output.append(pdf_inserted)
    output.merge(page_index, pdf_insert)
    with open(merged_name, 'wb') as f:
        output.write(f)
        print('Insert Success')


if __name__ == "__main__":
    base = os.getcwd()
    orignal_path = base + 'test1.pdf'
    insert_path = base + 'test2.pdf'
    new_path = base + 'insert.pdf'
    Insert(orignal_path, insert_path, 1, new_path)
