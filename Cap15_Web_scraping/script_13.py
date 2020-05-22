from bs4 import BeautifulSoup

# with open('simple.html', 'r') as file_reader:
# for line in file_reader.readlines():
#     print(line, end='')

# Parseando o arquivo html
# with open('simple.html', 'r') as file_reader:
#     soup = BeautifulSoup(file_reader, 'html.parser')
#     print(soup.prettify())

# Exibindo o conteudo das TAGs
# with open("simple.html", "r") as file:
#     contents = file.read()
#     soup = BeautifulSoup(contents, 'lxml')
#     print(soup.h2)
#     print(soup.head)
#     print(soup.li)
#     print(soup.p)

# Exbindo todas as TAGS
# with open("simple.html", "r") as file:
#     contents = file.read()
#     soup = BeautifulSoup(contents, 'lxml')
#     for child in soup.recursiveChildGenerator():
#         if child.name:
#             print(child.name)


# Exibindo uma TAG e sua TAG Parent
# with open("simple.html", "r") as file:
#     soup = BeautifulSoup(file, 'lxml')
#     print(soup.title)
#     print(soup.title.text)
#     print(soup.title.parent)

# INSERINDO ELEMENTOS
with open("simple.html", "r") as file:
    contents = file.read()
    soup = BeautifulSoup(contents, 'lxml')
    newtag = soup.new_tag('li') # INSERINDO UMA LISTA <li>
    newtag.string='OpenBSD'
    ultag = soup.ul
    ultag.insert(2, newtag)
    print(ultag.prettify())

# Alterando conteudo
# with open("simple.html", "r") as file:
#     contents = file.read()
#     soup = BeautifulSoup(contents, 'lxml')
#     print(soup.p)
#     print(soup.p.text)
#     new_txt = 'Linux is a Amazing Operate System'
#     tag = soup.p
#     tag.string = new_txt
#     print(soup.prettify())


with open("simple.html", "r") as file:
    with open('simple_atualizado.html', 'w') as html_writer:
        contents = file.read()
        soup = BeautifulSoup(contents, 'lxml')
        new_txt = 'Linux is a Amazing Operate System'
        tag = soup.p
        tag.string = new_txt
        content = soup.prettify()
        html_writer.write(content)
    print('Done...')