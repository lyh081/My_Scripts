# photo_rename_time.py
# __author__ = 'Henry Liu'
# __version__ = '1.0'

"""
This can rename photos in an given directory according to the time it was taken.
"""

import exifread
import os
import re


def getFileName(path):
    """ 
    Get all the photos(jpg or jpeg) in the given dictionary
    Return a photo_path list
    """
    pattern = r"\.jpeg|\.jpg$"
    file_name_lst = [os.path.join(path, f) for f in os.listdir(
        path) if re.search(pattern, f, re.IGNORECASE)]
    return file_name_lst


def rename(file_path, time):
    """ 
    Rename photo to the'time-originalname' pattern
    """
    p = file_path.split('\\')
    new_name = '\\'.join(p[:-1]) + '\\' + time + '-' + p[-1]
    os.rename(file_path, new_name)


def get_Time_info(file_lst):
    """
    Get Image Datetime info and rename it 
    """
    for fil in file_lst:
        f = open(fil, 'rb')
        tags = exifread.process_file(f)
        f.close()
        time = str(tags.get('Image DateTime')).replace(' ', '-')

        if time == 'None':
            print("Photo {} don't have time info.".format(fil))
        else:
            rename(fil, time.replace(':', '-'))
            print('Rename photo on {} Done!'.format(time))


def main(path):
    file_lst = getFileName(path)
    get_Time_info(file_lst)


if __name__ == "__main__":
    base = os.getcwd()
    main(base)
