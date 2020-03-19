#!/usr/bin/env pytho      
# -*- coding: utf-8 -*-
name = 'tom'
age = 12
weight = 75.6
# 我叫X，今年X岁了，体重X公斤
print('我叫%s，今年%s岁了，体重%s公斤' % (name, age, weight))

print(f'我叫{name}，今年{age}岁了，体重{weight}公斤')   # 比上一种更高效，Python3.6之后版本有
