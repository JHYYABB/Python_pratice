# coding:utf-8

'''
Author: 知会_X
Date: 2021-11-17 14:59:38
LastEditTime: 2021-11-17 16:11:38
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Python编程：从入门到实践\第2章;变量和简单数据类型.py
'''


start_up = 2.3

while True:
    if start_up == 2.3:
        user_name = "Eric"
        message = "would you like to learn some Python today?"
        print("Hello "+user_name+","+message)
    elif start_up == 2.4:
        user_name = "Eric"
        print(user_name.lower())
        print(user_name.upper())
        print(user_name.title())
    elif start_up == 2.5 or start_up == 2.6:
        famous_person = "Albert Einstein "
        speak = "once said, "
        message = '“A person who never madea mistake never tried anything new.”'
        print(famous_person+speak+message)
    elif start_up == 2.7:
        user_name = "  Eric "
        print('\t*'+user_name.lstrip()+'*\n')
        print('\t*'+user_name.rstrip()+'*\n')
        print('\t*'+user_name.strip()+'*\n')
    elif start_up == 2.8:
        print(4+4)
        print(2*4)
        print(16-8)
        print(16/2)
        break
    start_up = int((start_up+0.1)*100)/100  # 去除精度误差

print("FNISH!!!")

"""
        题后终结：
        1.浮点数做运算的时候并不像c那样精确，例如：2.7+0.1并不等于2.8
        详细原因参考网址：https://blog.csdn.net/xufive/article/details/
                        103816159?ops_request_misc=%257B%2522request%2
                        55Fid%2522%253A%2522163713408316780261969767%2
                        522%252C%2522scm%2522%253A%252220140713.130102
                        334.pc%255Fall.%2522%257D&request_id=163713408
                        316780261969767&biz_id=0&utm_medium=distribute
                        .pc_search_result.none-task-blog-2~all~first_r
                        ank_ecpm_v1~rank_v31_ecpm-1-103816159.pc_searc
                        h_result_cache&utm_term=python+%E8%87%AA%E5%8A
                        %A00.1&spm=1018.2226.3001.4187
"""
