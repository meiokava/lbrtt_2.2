#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = int(input('enter digit (the rage is from 1 to 4): '))
    if a == 1:
        print('it is winter')
    elif a == 2:
        print('it is spring')
    elif a == 3:
        print('it is summer')
    elif a == 4:
        print('it is autumn')
    else:
        print('error choose within a range')
