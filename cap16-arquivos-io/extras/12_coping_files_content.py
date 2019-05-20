#!/usr/bin/env python3

with open('foo2.txt', 'r') as rf:
    with open('foo3.txt', 'w') as wf:
        for line in rf:
            wf.write(line)


print('Done!')