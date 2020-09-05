#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 
import re
def txt_clean(x):
    pattern = re.compile(r'<\w*>|</\w*>')
    result = pattern.search(x)
    return result
def main():
	path = '/Users/zach/PycharmProjects/day1/en-zh/'
    # file = 'train.tags.en-zh.en'
    # save_path = '/Users/zach/PycharmProjects/day1/en-zh/train.en'

    file = 'train.tags.en-zh.zh'
    save_path = '/Users/zach/PycharmProjects/day1/en-zh/train.zh'
    path1 = path + file

    output = open(save_path, 'w', encoding='utf-8')
    with open(path1, 'r', encoding='utf-8') as f:
    	x = f.readlines()
        for y in x:
            result = txt_clean(y)
            # print(result)
            if result is None:
                # print(y)
                output.write(y)
    output.close()
if __name__ == '__main__':
    main()