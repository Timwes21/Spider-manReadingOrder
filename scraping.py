from bs4 import BeautifulSoup
import requests
amazing_title = []
spectacular_title = []
web_of_title = []

def sparse(page, new_title):
    for ul in page:
        raw_text = ul.text.strip()
        titles = raw_text.split('\n')
        for title in titles:
            cleaned_title = title.strip()
            if cleaned_title:
                new_title.append(cleaned_title)

    return new_title

def get_list(url, new_title):
    spiderman_page = requests.get(url).text
    soup = BeautifulSoup(spiderman_page, 'lxml')
    page = soup.find_all('ul', class_="list-story") #The site uses the same class name for each list
    new_title = sparse(page, new_title)
    return new_title

amazing_title = get_list("https://readallcomics.com/category/amazing-spider-man/", amazing_title)
spectacular_title = get_list("https://readallcomics.com/category/peter-parker-the-spectacular-spider-man-1/", spectacular_title)
web_of_title = get_list("https://readallcomics.com/category/web-of-spider-man/", web_of_title)



