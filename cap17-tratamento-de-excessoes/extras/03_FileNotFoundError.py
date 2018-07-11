#!/usr/biin/env python3

try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf_Error:
    print("Arquivo nao encontrado",fnf_Error)