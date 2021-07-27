from bs4 import BeautifulSoup

# with open("books.xml","r") as file_reader:
#     contents = file_reader.read()
#     soup = BeautifulSoup(contents,'xml')
#     titles = soup.find_all('title')
#     for title in titles:
#         print(title.get_text())


with open("books.xml","r") as file_reader:
    contents = file_reader.read()
    soup = BeautifulSoup(contents,'xml')
    titles = soup.find_all('title')
    authors = soup.find_all('author')
    prices = soup.find_all('price')
    for i in range(0, len(titles)):
        print(titles[i].get_text(),"by", end=' ')
        print(authors[i].get_text(), end=' ')
        print("costs $" + prices[i].get_text())

# with open('arquivo_tributario.xml', 'r') as xml_reader:
#     contents = xml_reader.read()
#     soup = BeautifulSoup(contents,'xml')
#     #print(soup)
#     conteudo = soup.find_all('D')
#     # cabecalho
#     print(conteudo[0])
#     print(conteudo[1])
#     print(conteudo[2])
#     print(conteudo[3])
#     print(conteudo[4])
#     print(conteudo[5])
#     # valores
#     print(conteudo[6])