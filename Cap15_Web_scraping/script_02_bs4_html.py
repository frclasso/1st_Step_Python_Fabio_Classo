import requests
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
print(page.status_code)
print(page.headers)
print(page.content)



# pip install bs4 lxml

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())

print()
# print(list(soup.children))
for tags in list(soup.children):
    print(tags)


print()
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.find_all('p'))
print(soup.find_all('p')[0].get_text())


"""
    Mais sobre Beautiful Soup
    https://www.dataquest.io/blog/web-scraping-tutorial-python/
"""