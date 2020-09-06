#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 
'''
import codecs 
import collections
from operator import itemgetter
 
RAW_DATA = 'simple-examples/data/ptb.train.txt' # 训练集数据文件
VOCAB_OUTPUT = 'ptb.vocab'      # 输出的词汇表文件

counter = collections.Counter()
with codecs.open(RAW_DATA, 'r', 'utf-8') as f:
    for line in f:
        for word in line.strip().split():
            counter[word] +=1

# 按词频顺序对单词进行排序
sorted_word_to_cnt = sorted(counter.items(), key=itemgetter(1), reverse=True)
sorted_words = [x[0] for x in sorted_word_to_cnt]
 
# 把句子结束符<eos>添加到词汇表中
sorted_words = ['<eos>'] + sorted_words
 
# 一般情况下，还需要把词汇表中删除低频词汇，在PTB数据中，因为输入数据已经将低频词汇替换成'<unk>'，
# 因此不需要这一步骤。
 
with codecs.open(VOCAB_OUTPUT, 'w', 'utf-8') as file_output:
    for word in sorted_words:
        file_output.write(word + '\n')
'''
import codecs
import sys
 
VOCAB = 'data/ptb.vocab'      # 输出的词汇表文件
TRAIN_RAW_DATA = 'simple-examples/data/ptb.train.txt' # 训练集数据文件
TRAIN_OUTPUT_DATA = 'data/ptb.train'
 
VALID_RAW_DATA = 'simple-examples/data/ptb.valid.txt' # 验证集数据文件
VALID_OUTPUT_DATA = 'data/ptb.valid'
 
TEST_RAW_DATA = 'simple-examples/data/ptb.test.txt' # 测试集数据文件
TEST_OUTPUT_DATA = 'data/ptb.test'

# 读取词汇表，并建立词汇到单词编号的映射
with codecs.open(VOCAB, 'r', 'utf-8') as f_vocab:
    vocab = [w.strip() for w in f_vocab.readlines()]
word_to_id = {k:v for (k, v) in zip(vocab, range(len(vocab)))}
 
# 如果出现被删除的低频词，则替换为'<unk>'
def get_id(word):
    return word_to_id[word] if word in word_to_id else word_to_id['<unk>']

def transfter_data(input_file_path, output_file_path):
    fin = codecs.open(input_file_path, 'r', 'utf-8')
    fout = codecs.open(output_file_path, 'w', 'utf-8')
 
    for line in fin:
        # 每个句子末尾增加句子结束符'<eos>'
        words = line.strip().split() + ['<eos>']
        out_line = ' '.join([str(get_id(w)) for w in words]) + '\n'
        fout.write(out_line)
 
    fin.close()
    fout.close()

transfter_data(TRAIN_RAW_DATA, TRAIN_OUTPUT_DATA)
transfter_data(VALID_RAW_DATA, VALID_OUTPUT_DATA)
transfter_data(TEST_RAW_DATA, TEST_OUTPUT_DATA)

