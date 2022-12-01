#!/usr/bin/python3
for i in range(97,123):
    i = chr(i)
    if i not in 'qe':
        print('{}'.format(i), end='')
