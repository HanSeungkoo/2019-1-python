import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.daum.net/")
soup = BeautifulSoup(req.text, 'html.parser')
titles = soup.find_all('span',{'class':'txt_issue'})

for x in titles:
    print(x.get_text())