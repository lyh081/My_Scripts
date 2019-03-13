import exifread
import re
import json
import requests


def get_GPS_Info(image_path):
    """
    获取图片的经纬度信息
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
    将解析得到的经纬度转换为十进制
    """
    deg, min, sec = [x.replace(' ', '')
                     for x in str(Lng_or_Lat)[1:-1].split(',')]
    formet_sec = (float(sec.split('/')[0]) / float(sec.split('/')[-1])) / 3600
    return float(deg) + float(min) / 60 + formet_sec


def find_address_from_GPS(GPS):
    """
    使用百度地图 API把经纬度坐标转换为结构化地址。
    """
    # 百度地图API秘钥，本秘钥来自互联网搜索，侵删（可自行申请）
    secret_key = '4IU3oIAMpZhfWZsMu7xzqBBAf6vMHcoa'
    if not GPS:
        return '无GPS信息'
    lat, lng = GPS['GPSLatitude'], GPS['GPSLongitude']
    baidu_map_api = （"http://api.map.baidu.com/geocoder/v2/?ak={0}&callback=renderReverse&location={1},{2}s&output=json&pois=0".format(secret_key, lat, lng)）
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
