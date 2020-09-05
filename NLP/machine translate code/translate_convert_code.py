#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

import codecs

def deal(lang):
    # 训练集数据文件
    ROOT_PATH = "/Users/zach/PycharmProjects/day1/en-zh/"
    if lang == "zh":
        # 原始的训练集数据文件
        RAW_DATA = ROOT_PATH + "test.zh"
        # 上面生成的词汇表文件
        VOCAB = ROOT_PATH + "zh.vocab"
        # 将单词替换成为单词编号后的输出文件
        OUTPUT_DATA = ROOT_PATH + "zh.number"
    elif lang == "en":
        RAW_DATA = ROOT_PATH + "test.en"
        VOCAB = ROOT_PATH + "en.vocab"
        OUTPUT_DATA = ROOT_PATH + "en.number"
    else:
        print("what?")

    # 读取词汇表，并建立词汇到单词编号的映射。
    with codecs.open(VOCAB, "r", "utf-8") as f_vocab:
        vocab = [w.strip() for w in f_vocab.readlines()]
    word_to_id = {k: v for (k, v) in zip(vocab, range(len(vocab)))}

    # 如果出现了被删除的低频词，则替换为"<unk>"。
    def get_id(word):
        return word_to_id[word] if word in word_to_id else word_to_id["<unk>"]
    
    fin = codecs.open(RAW_DATA, "r", "utf-8")
    fout = codecs.open(OUTPUT_DATA, 'w', 'utf-8')
    for line in fin:
        # 读取单词并添加<eos>结束符
        words = line.strip().split() + ["<eos>"]
        # 将每个单词替换为词汇表中的编号
        out_line = ' '.join([str(get_id(w)) for w in words]) + '\n'
        fout.write(out_line)
    fin.close()
    fout.close()

if __name__ == "__main__":
    # 处理的语言
    lang = ["zh", "en"]
    for i in lang:
        deal(i)

