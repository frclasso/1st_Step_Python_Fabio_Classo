#!/usr/bin/env python3

with open('tecnologias.txt', 'r') as rf:
    with open('copia_tecnologias.txt', 'w') as wf:
        for line in rf:
            wf.write(line)


print('Done!')