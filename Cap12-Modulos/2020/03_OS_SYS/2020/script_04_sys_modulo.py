import sys

print(f'Maior numero inteiro possivel: {sys.maxsize}')


print(f'Path: {sys.path}')
for path in sys.path:
    print(path)


print()
print(f'Paltaforma: {sys.platform}')