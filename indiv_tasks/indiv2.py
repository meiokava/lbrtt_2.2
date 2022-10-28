#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    x = int(input('enter a: '))
    y = int(input('enter b: '))
    if x**2 + y**2 == 1:
        print('these coordinates belong to circle x^2 + y^2 = 1')
    elif x**2 + y**2 == 0.25:
        print('these coordinates belong to circle x^2 + y^2 = 0.25')
    else:
        print('these coordinates dont belong to circle')
