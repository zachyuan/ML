#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

import numpy as np
import tensorflow as tf
 
TRAIN_DATA = 'data/pb.train' # 使用单词编号表示的训练数据
TRAIN_BATCH_SIZE = 20
TRAIN_NUM_STEP = 35
 
# 从文件中读取数据，并返回包含单词编号的数组
def read_data(file_path):
    with open(file_path, 'r') as fin:
        id_string = ' '.join([line.strip() for line in fin.readlines()])
    id_list = [(int)(w) for w in id_string.split()]
    return id_list
 
 
def make_batches(id_list, batch_size, num_step):
    # 计算总的batch数量，每个batch包含的单词数量是batch_size*num_step
    num_batches = (len(id_list)-1)// (batch_size*num_step)
    
    # 将数据整理成一个维度为[batch_size, num_batches*num_step]的二维数组
    data = np.array(id_list[:num_batches*batch_size*num_step])
    print('data shape={}, data:{}\n'.format(data.shape, data[:1]))
    data = np.reshape(data, [batch_size, num_batches*num_step])
    print('data shape={}, data:{}\n'.format(data.shape, data[:1]))
    
    # 沿着第二个维度将数据切分（纵轴方向往下切）成num_batches个batch，存入一个数组。
    data_batches = np.split(data, num_batches, axis=1)
    print('data_batches len={}, data_batches:{}'.format(len(data_batches), data_batches[:1]))
    
    # 重复上述操作，但是每个位置向右移动一位，这里得到的是RNN每一步输出所需要的预测的下一个单词
    label = np.array(id_list[1:num_batches*batch_size*num_step + 1])
    label = np.reshape(label, [batch_size, num_batches*num_step])
    label_batches = np.split(label, num_batches, axis=1)
    
    #返回一个长度为num_batches的数组，其中每一项包括一个data矩阵和一个label矩阵。
    return list(zip(data_batches, label_batches))
 
train_batches = make_batches(read_data(TRAIN_DATA), TRAIN_BATCH_SIZE, TRAIN_NUM_STEP)



# a = [
#     1, 2, 3, 4, 
#     5, 6, 7, 8, 
#     9, 10, 11, 12,
# ]
# a = np.array(a)
# print('a shape={}, a:{}\n'.format(a.shape, a))
# a.shape = (3, 4)
# print('a shape={}, a:\n{}\n'.format(a.shape, a))
 
# print(np.split(a, 2, axis=1))