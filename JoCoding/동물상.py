from urllib.request import urlopen

from bs4 import BeautifulSoup

with urlopen('https://trends.google.co.kr/trends/trendingsearches/daily?geo=KR') as response:
    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.select('div.title'):
        print(anchor)
