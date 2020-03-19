#!/usr/bin/env pytho      
# -*- coding: utf-8 -*-
"""
1.准备数据
2.格式化符号输出
"""
age = 18
name = '张三'
weight = 53.2
stu_id = 1

# 1.今年我的年龄是X岁
print('今年我的年龄是%d岁' % age)

# 2.我的名字是X
print('我的名字是%s' % name)

# 3.我的体重是X公斤
print('我的体重是%.2f公斤' % weight)

# 4.我的学号是X
print('我的学号是%d' % stu_id)
# 4.1 我的学号是001
print('我的学号是%03d' % stu_id)     # 不足3位用0补齐，超出原样输出
stu_id2 = 1234
print('我的学号是%03d' % stu_id2)

# 5.我的名字是X，今年X岁
print('我的名字是%s，今年%d岁' % (name, age))
# 5.1 我的名字是X，明年X岁
print('我的名字是%s，明年%d岁' % (name, age + 1))

# 6.我的名字是X，今年X岁了，体重X公斤，学号是X
print('我的名字是%s，今年%d岁了，体重%.2f公斤，学号是%06d' % (name, age, weight, stu_id))