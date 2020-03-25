#!/usr/bin/env pytho      
# -*- coding: utf-8 -*-
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f'{i}*{j}={i*j}', end='\t')
        j += 1
    i += 1
    print()
