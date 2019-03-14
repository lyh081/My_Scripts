# photo_rename_time.py
# __author__ = 'Henry Liu'
# __version__ = '1.0'

"""
This can analyze photo's GPS information
and convert it to structured address by using Baidu Map API
"""

import exifread
import json
import requests


def get_GPS_Info(image_path):
    """
    Get the GPS (latitude and longitude) information of the image
    """
    GPS = {}
    date = ''
    with open(pic_path, 'rb') as f:
        tags = exifread.process_file(f)
        GPS = {
            'GPSLatitudeRef': str(tags.get('GPS GPSLatitudeRef')),
            'GPSLatitude': convert(tags.get('GPS GPSLatitude')),
            'GPSLongitudeRef': str(tags.get('GPS GPSLongitudeRef')),
            'GPSLongitude': convert(tags.get('GPS GPSLongitude'))
        }
    return GPS


def convert(Lng_or_Lat):
    """
    Convert the latitude/longitude to decimal number
    """
    deg, min, sec = [x.replace(' ', '')
                     for x in str(Lng_or_Lat)[1:-1].split(',')]
    formet_sec = (float(sec.split('/')[0]) / float(sec.split('/')[-1])) / 3600
    return float(deg) + float(min) / 60 + formet_sec


def find_address_from_GPS(GPS):
    """
    Convert decimal latitude/longitude to convert it to structured address by using Baidu Map API
    """
    # This secret_key was collected from internet, you can apply for a free one
    secret_key = '4IU3oIAMpZhfWZsMu7xzqBBAf6vMHcoa'
    if not GPS:
        return "This photo dosn't GPS information."
    lat, lng = GPS['GPSLatitude'], GPS['GPSLongitude']

    baidu_map_api = "http://api.map.baidu.com/geocoder/v2/?ak={0}&callback=renderReverse&location={1},{2}s&output=json&pois=0".format(
        secret_key, lat, lng)
    response = requests.get(baidu_map_api)

    content = response.text.replace("renderReverse&&renderReverse(", "")[:-1]
    baidu_map_addr = json.loads(content)
    address = {
        'formatted_address': baidu_map_addr["result"]["formatted_address"],
        'sematic_description': baidu_map_addr["result"]["sematic_description"],
    }

    return address


if __name__ == "__main__":
    pic_path = 'test.jpg'
    GPS = get_GPS_Info(pic_path)
    address = find_address_from_GPS(GPS)
    print(address)
