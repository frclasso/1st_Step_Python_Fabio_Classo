#!/usr/bin/env python3

import sys, os


def main():
    v = sys.version_info
    print('Python version {}.{}.{}'.format(*v))

    w = sys.platform
    print(f"Plataforma: {w}")

    z = os.name
    print(f"OS name: {z}")
    print()

    y = os.getenv('PATH')  # imprime variaveis de ambiente
    print(f"Variaveis de ambiente:{y}")
    print()

    i = os.getcwd()  # imprime diretorio local
    print(f"Diretorio atual: {i}")
    print()

    # imprime o PATH do arquivo e da instalacao do Python
    for p in sys.path: print(f"PATH: {p}")


if __name__=="__main__":main()
