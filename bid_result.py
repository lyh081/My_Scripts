import io, requests, pytesseract
from PIL import Image
from wxpy import *
from bs4 import BeautifulSoup
from threading import Timer

pytesseract.pytesseract.tesseract_cmd = 'D:\Program Files (x86)\Tesseract-OCR/tesseract.exe'  # tesseract安装地址


# 请求网页并解析
def get_html(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    return soup


# 若投标结果已出，返回项目链接
def project_url(html, name):

    projects = html.select('.c1-body li')
    url = None

    for project in projects[:5]:
        if name in project.a.attrs['title']:
            url = project.a.attrs['href']
    return url


# 返回中标结果
def bid_result(html):

    img_url = html.select('.frameNews img')[0].attrs['src']
    img_content = requests.get(img_url).content # 获取项目结果页图片

    # 将结果图片保存到本地
    with open('result.jpg', 'wb') as f:
        f.write(img_content)
    
    # 将请求到的数据转换为Bytes字节流，并用PIL打开
    img_byte = io.BytesIO(img_content)
    img = Image.open(img_byte)

    # 利用tesseract ocr引擎识别图片字符
    result = pytesseract.image_to_string(img,lang='chi_sim')

    if u'宁 波 城 建 设 计' in result：
        send2wechat('Success')
    else:
        send2wechat('Fail')


def send2wechat(info):
    # 使用微信发送投标结果，可改为发送给某个朋友
    bot.file_helper.send(info)


def main():
    base_url = 'http://www.bidding.gov.cn/gcjszbgg1'
    index = '/index.htm' 
    index_soup = get_html(base_url+index)
    bid_url = project_url(index_soup, u'东钱湖供水一体化')
    if bid_url:
        bid_result(get_html(bid_url))
    else:
        print(u'Without Result Now。')
    timer = Timer(300,main) # 定时5分钟（300s）执行一次
    timer.start()

if __name__ == '__main__':
    bot = Bot(cache_path=True)
    timer = Timer(300,main)
    timer.start()
