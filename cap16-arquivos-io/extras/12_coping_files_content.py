#!/usr/bin/env python3

with open('arquivo.txt', 'r') as rf:
    with open('arquivo_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

print('Done!')