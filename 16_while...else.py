#!/usr/bin/env pytho      
# -*- coding: utf-8 -*-

# 当while循环正常结束后，执行else下的代码
# i = 1
# while i <= 5:
#     print(f'打印{i}遍')
#     i += 1
# else:
#     print("5遍打印成功")


# break属于非正常执行
# i = 1
# while i <= 5:
#     if i == 3:
#         print('打印失败')
#         break
#     print(f'打印{i}遍')
#     i += 1
# else:
#     print("5遍打印成功")  # 不打印


# continue属于正常执行
i = 1
while i <= 5:
    if i == 3:
        print('打印失败')
        i += 1
        continue
    print(f'打印{i}遍')
    i += 1
else:
    print("5遍打印成功")  # 打印
