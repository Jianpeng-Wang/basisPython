#!/usr/bin/env pytho      
# -*- coding: utf-8 -*-
mystr = "hello world and python and pycharm"

# 1.find函数  rfind：从右边开始
# print(mystr.find('and'))  # 12
# print(mystr.find('and', 15, 30))  # 23
# print(mystr.find('ands'))  # -1  找不到

# 2.index函数 rfind：从右边开始
# print(mystr.index('and'))  # 12
# print(mystr.index('and', 15, 30))  # 23
# print(mystr.index('ands'))  # 报错  找不到

# 3.count函数
print(mystr.count('and'))  # 2
print(mystr.count('and', 15, 30))  # 1
print(mystr.count('ands'))  # 0  找不到


