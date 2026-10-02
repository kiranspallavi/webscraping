import requests
from bs4 import BeautifulSoup

u_id=input("Enter the topic : ")

url="https://en.wikipedia.org/wiki/"+u_id

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

for h in soup.find_all("h2"):
    print(h.text)

a=input("What Section do you want? ")
a=str.istitle(a)


head=soup.find("h2",id=a)

for p in head.find_all_next():
    if p.name=="p":
        print(p.get_text(strip=True))
    if p.name=="h2":
        break