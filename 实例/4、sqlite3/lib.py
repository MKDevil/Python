'''
Author: MK_Devil
Date: 2022-01-14 17:01:01
LastEditTime: 2022-01-14 17:09:25
LastEditors: MK_Devil
'''


def del_repeat(x):
    result_list = []
    for i in x:
        if i not in result_list:
            result_list.append(i)
    return result_list
