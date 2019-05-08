import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.daum.net/")
soup = BeautifulSoup(req.text, 'html.parser')
titles = soup.select('div.roll_txt').select('div.rank_count').select('span.txt_issue').select('a.link_issue')[0]

for x in ex_list:
    print(x.text)