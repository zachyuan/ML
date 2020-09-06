#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

# 定义一个基本的LSTM结构作为循环体的基础结构
lstm_cell = tf.nn.rnn_cell.BasicLSTMCell

# 通过MultiRNNCell类实现深层循环神经网络中每一个时刻的前向传播过程。
# number_of_layers表示有多少层
# 注意：从TensorFlow1.1版本起，不能使用[lstm_cell(lstm_size)] * N的形式来初始化MultiRNNCell，
# 否则TensorFlow会在每一层之间共享参数。
stacked_lstm = tf.nn.rnn_cell.MultiRNNCell(
    [lstm_cell(lstm_size) for _ in range(number_of_layers)]
)

# 和经典的循环神经网络一样，可以通过zero_state来获取初始状态
state = stacked_lstm.zero_state(batch_size, tf.float32)

# 计算每一时刻的前向传播结果
for i in range(len(num_steps)):
    if i > 0: tf.get_variable_scope().reuse_variables()
        
    stacked_lstm_output, state = stacked_lstm(current_input, state)
    final_output = fully_connected(stacked_lstm_output)
    loss += calc_loss(final_output, expected_output)


'''
# 定义LSTM结构
lstm_cell = tf.nn.rnn_cell.BasicLSTMCell
# 使用DropoutWrapper类实现dropout功能。该类通过两个参数来控制dropout的概率，
# 一个参数为Input_keep_prob，可以控制输入的dropout概率；另一个为output_keep_prob，它可以用来控制输出的dropout概率。
stacked_lstm = tf.nn.rnn_cell.MultiRNNCell(
    [tf.nn.rnn_cell.DropoutWrapper(lstm_cell(lstm_size)) for _ in range(number_of_layers)]
)
 
'''
