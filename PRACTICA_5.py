import requests
from bs4 import BeautifulSoup as bs

url = "https://www.bbc.com/mundo/topics/c340qyp6yggt"
pag = requests.get(url)
soup = bs(pag.content, "html.parser")
info = soup.find_all("a", "qa-heading-link lx-stream-post__header-link")

print("Noticias del dia de hoy en Mexico.")

for i in info:
    sub = i.find_all("span")
    sun = i.attrs.get("href")

    print(sub[0].contents[0])
    print(url + sun)
    print("")
