# coding:utf-8
'''
Author: your name
Date: 2021-11-17 17:19:03
LastEditTime: 2021-11-17 17:23:48
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Python编程：从入门到实践\第3章；列表简介.py
'''
start_up = 3.2

while True:
    if start_up == 3.1:
        names = ['Xm','Xh','Xd','Xz']
        for x in names:
            print(x)
    elif start_up == 3.2:
        names = ['Xm','Xh','Xd','Xz']
        message = "Hello my name is "
        for x in names:
            print(message+x)
        break
        