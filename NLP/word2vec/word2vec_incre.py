#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

import jieba
import re
import pandas as pd
from gensim.models.word2vec import Word2Vec

class TrainWord2Vec:
    """
    训练得到一个Word2Vec模型
    """
    def __init__(self, data, stopword, num_features=100, min_word_count=1, context=4, incremental=False,
                 old_path):
        """
        定义变量
        :param data: 用于训练胡语料
        :param stopword: 停用词表
        :param num_features:  返回的向量长度
        :param min_word_count:  最低词频
        :param context: 滑动窗口大小
        :param incremental: 是否进行增量训练
        :param old_path: 若进行增量训练，原始模型路径
        """
        self.data = data
        self.stopword = stopword
        self.num_features = num_features
        self.min_word_count = min_word_count
        self.context = context
        self.incremental = incremental
        self.old_path = old_path
    def clean_text(self):
        """
        采用结巴分词函数分词
        :param corpus: 待分词的Series序列
        :return: 分词结果，list
        """
        # 去除无用字符
        pattern = re.compile(r'[\sA-Za-z～()（）【】%*#+-\.\\\/:=：__,，。、;；“”""''’‘？?！!<《》>^&{}|=……]')
        corpus_ = self.data.apply(lambda s: re.sub(pattern, '', s))
        # 分词
        text = corpus_.apply(jieba.lcut)
        # 过滤通用词
        text = text.apply(lambda cut_words: [word for word in cut_words if word not in self.stopword])
        return text
    def get_model(self, text):
        """
        从头训练word2vec模型
        :param text: 经过清洗之后的语料数据
        :return: word2vec模型
        """
        model = Word2Vec(text, size=self.num_features, min_count=self.min_word_count, window=self.context)
        return model
    def update_model(self, text):
        """
        增量训练word2vec模型
        :param text: 经过清洗之后的新的语料数据
        :return: word2vec模型
        """
        model = Word2Vec.load(self.old_path)  # 加载旧模型
        model.build_vocab(text, update=True)  # 更新词汇表
        model.train(text, total_examples=model.corpus_count, epochs=model.iter)  # epoch=iter语料库的迭代次数；（默认为5）  total_examples:句子数。
        return model
    def main(self):
        """
        主函数，保存模型
        """
        # 加入自定义分析词库
        jieba.load_userdict("add_word.txt")
        text = self.clean_text()
        if self.incremental:
            model = self.update_model(text)
        else:
            model = self.get_model(text)
        # 保存模型
        model.save("word2vec.model")

if __name__ == '__main__':
    corpus = pd.read_csv("corpus.csv", encoding='gbk')
    stop_word = pd.read_csv("stopword.csv", encoding='gbk')
    trainmodel = TrainWord2Vec(data=corpus, stopword=stop_word)
    trainmodel.main()