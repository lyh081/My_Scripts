from PyPDF2 import PdfFileReader, PdfFileMerger, PdfFileWriter
import os
import re


def getFileName(path):
    pattern = r"\.pdf$"
    file_names_lst = [path + "\\" + f for f in os.listdir(path) if re.search(
        pattern, f, re.IGNORECASE)]
    # print(file_names_lst)
    return file_names_lst


def Merge_all(file_lst, mergedpath):
    pdfMerge = PdfFileMerger()
    opened_files = [open(file_name, 'rb') for file_name in file_lst]
    for opened_file in opened_files:
        pdfMerge.append(opened_file)
    with open(mergedpath, 'wb') as out_file:
        pdfMerge.write(out_file)
    for opened_file in opened_files:
        opened_file.close()
    print('Done!')


if __name__ == "__main__":
    path = os.getcwd()
    file_lst = getFileName(path)
    Merge(file_lst, path+'\\Merge.pdf')
