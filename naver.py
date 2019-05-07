import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.naver.com/")
soup = BeautifulSoup(req.text, 'html.parser')
titles = soup.find_all('span',{'class':'ah_k'})

for x in titles:
    print(x.get_text())