#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    school = []
    # заполняем словарь
    school = {
        '1a': 20,
        '1b': 21,
        '2a': 21,
        '2c': 20,
        '3a': 19,
        '3b': 23,
    }
    # вывод списка
    for key, value in school.items():
        print('в классе ', key, ' учатся ', value)

    print('---- Изменения списка --------')

    school['1b'] = '25'
    del school['3a']
    school['4a'] = '22'

    for key, value in school.items():
        print('в классе ', key, ' учатся ', value)

    # кол-во учеников в школе
    s = 0
    for i in school:
        s = s + int(school[i])
    print("В школе учится: ", s)