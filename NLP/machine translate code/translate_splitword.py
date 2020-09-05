#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 
from stanfordcorenlp import StanfordCoreNLP
import time

# sentence1 = "大家想想，海洋占了地球面积的75％。"
# sentence2 = "When you think about it, the oceans are 75 percent of the planet."
# nlp = StanfordCoreNLP('/Users/zach/Documents/stanford-corenlp-4.1.0', lang='zh')
# fenci=nlp.word_tokenize(sentence1)
# seg_list = jieba.cut(sentence1, cut_all=False)
# tokens = nltk.word_tokenize(sentence2)
# print(fenci)
# print(list(seg_list))
# print(tokens)

path = '/Users/zach/PycharmProjects/day1/en-zh/'
en_path = path + 'train.en'
zh_path = path + 'train.zh'

seg_list = jieba.cut(sentence1, cut_all=False)
tokens = nltk.word_tokenize(sentence2)

# en = open(path + 'test.en', 'w', encoding='utf-8')
zh = open(path + 'test.zh', 'w', encoding='utf-8')
# with open(en_path, 'r', encoding='utf-8') as f:
with open(zh_path, 'r', encoding='utf-8') as f:
    data = f.readlines()
    for text in data:
        print(text)
        if text != "\n":
            fenci = jieba.cut(text, cut_all=False)
            # fenci = nltk.word_tokenize(text)
            # nlp = StanfordCoreNLP('/Users/zach/Documents/stanford-corenlp-4.1.0', lang='zh')
            # fenci=nlp.word_tokenize(text)
            sen = ' '.join(fenci)
            zh.write(sen + '\n')
            # en.write(sen + '\n')
        else:
            zh.write('\n')
            # en.write('\n')
zh.close()
en.close()

import codecs
import collections
from operator import itemgetter


def deal(lang):
    # 训练集数据文件
    ROOT_PATH = "/Users/zach/PycharmProjects/day1/en-zh/"
    if lang == "zh":
        RAW_DATA = ROOT_PATH + "test.zh"
        # 输出的词汇表文件
        VOCAB_OUTPUT = ROOT_PATH + "zh.vocab"
        # 中文词汇表单词个数
        VOCAB_SIZE = 4000
    elif lang == "en":
        RAW_DATA = ROOT_PATH + "test.en"
        VOCAB_OUTPUT = ROOT_PATH + "en.vocab"
        VOCAB_SIZE = 10000
    else:
        print("what?")
    # 统计单词出现的频率
    counter = collections.Counter()
    with codecs.open(RAW_DATA, "r", "utf-8") as f:
        for line in f:
            for word in line.strip().split():
                counter[word] += 1
    sorted_word_to_cnt = sorted(counter.items(), key=itemgetter(1), reverse=True)
    sorted_words = [x[0] for x in sorted_word_to_cnt]

    # 在后面处理机器翻译数据时，出了"<eos>"，还需要将"<unk>"和句子起始符"<sos>"加入
    # 词汇表，并从词汇表中删除低频词汇。在PTB数据中，因为输入数据已经将低频词汇替换成了
    # "<unk>"，因此不需要这一步骤。
    with codecs.open(VOCAB_OUTPUT, 'w', 'utf-8') as file_output:
        for word in sorted_words:
            file_output.write(word + "\n")

    with codecs.open(VOCAB_OUTPUT, 'w', 'utf-8') as file_output:
        for word in sorted_words:
            file_output.write(word + "\n")

if __name__ == "__main__":
    # 处理的语言
    lang = ["zh", "en"]
    for i in lang:
        deal(i)
        print(i)

