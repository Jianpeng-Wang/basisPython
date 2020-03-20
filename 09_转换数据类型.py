#!/usr/bin/env pytho      
# -*- coding: utf-8 -*-

num = 1
str1 = '10'
floatNum = 1.8
a = [10, 20, 30]
b = (100, 200, 300)
str2 = '1'
str3 = '1.1'
str4 = '(1000, 2000, 3000)'
str5 = '[1000, 2000, 3000]'

# int(),将数据转换成整型
print(int(str1), end=',')
print(type(int(str1)))
print(int(floatNum), end=',')
print(type(int(floatNum)))

# float(),将数据转换成浮点型
print(float(str1), end=',')
print(type(float(str1)))
print(float(num), end=',')
print(type(float(num)))

# str(),将数据转换成字符串
print(str(num), end=',')
print(type(str(num)))

# tuple(),将数据转换成元组
print(tuple(a))

# list(),将数据转换成列表
print(list(b))

# eval(),计算字符串中有效Python表达式，并返回一个对象
print(type(eval(str2)))
print(type(eval(str3)))
print(type(eval(str4)))
print(type(eval(str5)))
