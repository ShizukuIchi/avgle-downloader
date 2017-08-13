from bs4 import BeautifulSoup
import requests
import sys

m3u8Name = sys.argv[2]
url = sys.argv[1]

res = requests.get(url)

soup = BeautifulSoup(res.text,"html.parser")
m3u8Url = str(soup.source['src'])

res = requests.get(m3u8Url,stream=True)
if res.status_code == 200:
    with open('./videos/m3u8/'+m3u8Name,'wb') as f:
        for chunk in res:
            f.write(chunk)
    print m3u8Name+' downloaded'
