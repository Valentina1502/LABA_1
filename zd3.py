#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    dic = {1: 'Каждый', 2: 'Охотник', 3: 'Желает', 4: 'Знать'}
    print(dic)
    for key, value in dic.items():
        print(key, ' - ', value)
    swapped = dict(map(reversed, dic.items()))

    for key, value in swapped.items():
        print(key, ' - ', value)
    print(swapped)