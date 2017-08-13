from bs4 import BeautifulSoup
import requests
import sys

m3u8Name = sys.argv[1]

res = requests.get('https://avgle.com/video/45447/27%E7%A8%AE%E9%A1%9E%E3%81%AE%E3%83%91%E3%82%A4%E3%82%BA%E3%83%AA%E3%81%A7%E3%82%A4%E3%82%AF%E3%81%A3-%E3%81%8A%E3%81%A3%E3%81%B1%E3%81%84%E5%A4%A7%E4%B9%B1%E4%BA%A4-%E7%BE%8E%E7%AB%B9%E3%81%99%E3%81%9A-miae-051')

soup = BeautifulSoup(res.text,"html.parser")
m3u8Url = str(soup.source['src'])

res = requests.get(m3u8Url,stream=True)
if res.status_code == 200:
    with open('./videos/m3u8/'+m3u8Name,'wb') as f:
        for chunk in res:
            f.write(chunk)
    print m3u8Name+' downloaded'