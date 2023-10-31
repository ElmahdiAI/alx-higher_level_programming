#!/usr/bin/python3
for ch in range(97, 123):
    if chr(ch) not in 'qe':
        print(chr(ch), end='')
