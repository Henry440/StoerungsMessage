import requests
from bs4 import BeautifulSoup

from confs import URL, TITLE_TAG, HTML_FILTER,USER_AGENT
from treffer import Treffer

page = requests.get(URL, headers=USER_AGENT)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find_all(class_=HTML_FILTER)
work_data = []

for html in results:
    titel = html.find(TITLE_TAG)
    work_data.append(Treffer(titel, html))
    

print(len(work_data))