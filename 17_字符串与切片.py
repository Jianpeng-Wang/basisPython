#!/usr/bin/env pytho      
# -*- coding: utf-8 -*-
"""
1.字符串下标的作用
2.切片 语法：  字符串[开始下标:结束下标:步长值]
    步长为负数：倒序

"""

str1 = "abcdefg"
print(str1[0])  # 输出 a

str2 = "0123456789"

# print(str2[2:5:1])  # 234
# print(str2[2:5:2])  # 24
# print(str2[2:5])  # 234
# print(str2[:5])  # 01234
# print(str2[2:])  # 23456789
# print(str2[:])  # 0123456789

# print(str2[::-1])  # 9876543210
# print(str2[-4:-1])  # 678
print(str2[-4:-1:-1])  # 不能选出字符
