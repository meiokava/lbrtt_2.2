#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    ameba = 1
    time_list = [1, 2, 3, 4, 5, 6]
    for time in time_list:
        ameba *= 2
        print('after', time, 'hours it will be', ameba, 'cells')
