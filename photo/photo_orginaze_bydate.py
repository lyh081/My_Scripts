# photo_orginaze.py
# __author__ = 'Henry Liu'
# __version__ = '1.0'

"""
This can organize photos in an given directory according to the time it was taken.
Photos shoot on the same day will be moved to the same directory('given_directory/year/month/day').

"""

import exifread
import shutil
from datetime import datetime
import os
import re


def getFileList(path):
    """ Get all the photos(jpg or jpeg) in the given dictionary and return a photo_path list """
    pattern = r"\.jpg|\.jpeg$"
    file_lst = [os.path.join(path, f) for f in os.listdir(
        path) if re.search(pattern, f, re.IGNORECASE)]
    return file_lst


def mkdir(path):
    """ If given path does'n exits, create it """
    path = path.strip().rstrip("\\")
    if os.path.exists(path):
        print(path, 'Aleady Exits.')
    else:
        os.makedirs(path)
        print(path, 'Create Success!')


def photo_organize(file_lst):
    """ Move photo accroding to time"""
    base = '\\'.join(file_lst[0].split('\\')[:-1])
    for fil in file_lst:
        f = open(fil, 'rb')
        tags = exifread.process_file(f)
        f.close()
        time = str(tags.get('Image DateTime'))
        if time == 'None':
            break

        f_time = datetime.strptime(time, "%Y:%m:%d %H:%M:%S")
        new_path = os.path.join(
            base, str(f_time.year), str(f_time.month), str(f_time.day)
        )

        mkdir(new_path)
        shutil.move(fil, new_path, new_path)
        print('Move Done')


def main(path):
    photos_lst = getFileList(path)
    photo_organize(photos_lst)


if __name__ == "__main__":
    main('D:\\photo_test')
