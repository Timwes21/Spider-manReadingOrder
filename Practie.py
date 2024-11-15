from bs4 import BeautifulSoup
import requests
amazing_title = []
spectacular_title = []
other_titles = []



html_text = requests.get("http://www.comicsbackissues.com/comic-book-reading-order/spider-man-read-order-chronology/").text

soup = BeautifulSoup(html_text, 'lxml')
page = soup.find_all('td', class_='column-4')
spiderman_titles =[]


for titles in page:
    spiderman_titles.append(titles.text.replace("BUY", ""))

for title in spiderman_titles:
    if "Amazing" in title:
        amazing_title.append(title)
    elif "Spectacular" in title:
        spectacular_title.append(title)
    else:
        other_titles.append(title)


for title in amazing_title:
    print(title)
#for items in p:
#    if items == "amazing":
#        amazing_title.insert(items)
#    elif items == "spectacular":
#        spectacular_title.insert(items)

