#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/21 15:06
# @Author  : Aries
# @Site    : 
# @File    : nltkDemo04.py
# @Software: PyCharm
import nltk

def is_preprocess(document):
    sentences=nltk.sent_tokenize(document)
    sentences=[nltk.word_tokenize(sent) for sent in sentences]
    sentences=[nltk.pos_tag(sent) for sent in sentences]
    return sentences
# sentences=is_preprocess("the little yellow dog barked at the cat")[0]
# print(sentences)
# grammar="NP:{<DT>?<JJ>*<NN>}"
# cp=nltk.RegexpParser(grammar)
# result=cp.parse(sentences)
# print(result)

# sentences_news="the market fo system-management software for Digital's hardware is fragmented enough that a giant such as Computer Associates should do well there."
# sentences=is_preprocess(sentences_news)[0]
# grammar="NP:{<DT>?<JJ.*>*<NN.*>}"
# cp=nltk.RegexpParser(grammar)
# result=cp.parse(sentences)
# for re in result.subtrees():
#     if re.label()=="NP":
#         print(re)

# 分块器的使用使用正则表达进行词性的分块
#名词分块器
# grammar="NP:{<DT|PP\$>?<JJ>*<NN>}{<NNP>+}"#多个分块器

# 使用文本语料库进行分块探索
# cp=nltk .RegexpParser('CHUNK:{<V.*><TO><V.*>}')
# brown=nltk.corpus.brown
# for sent in brown.tagged_sents():
#     tree=cp.parse(sent)
#     for subtree in tree.subtrees():#数据结构是[(),(subtree.labels word lists)]
#         if(subtree.label()=="CHUNK"):
#             print(subtree)

#使用分块器进行的模型评估方式
from nltk.corpus import conll2000
# print(conll2000.chunked_sents("train.txt")[99])
# print(conll2000.chunked_sents("train.txt",chunk_types=["NP"])[99])
# cp=nltk.RegexpParser("")
# test_sents=conll2000.chunked_sents("test.txt",chunk_types=["NP"])
# print(cp.evaluate(test_sents))



# test_sents=conll2000.chunked_sents("test.txt",chunk_types=["NP"])
# grammar=r"NP:{<[CDJNP].*>+}"#将相应的词按照一定的正则进行分块，然后和已知词库进行比较准确性等
# cp=nltk.RegexpParser(grammar)
# print(cp.evaluate(test_sents))


#建立分类词块unigram模型用来根据前一个词的词块来预测后一个词的词块,通过词性到词块的映射，找到词块到词性的映射关系
class UnigramChunker(nltk.ChunkParserI):
    def __init__(self,train_sents):
        train_data=[[(t,c) for w,t,c in nltk.chunk.tree2conlltags(sent)] for sent in train_sents]
        #对每一词进行词性标注然后进行分块
        self.tagger=nltk.UnigramTagger(train_data)
    def parse(self,sentence):
        pos_tag=[pos for (word,pos) in sentence] #输入是[(),()]二元组数据结构
        tagged_pos_tags=self.tagger.tag(pos_tag)
        chunktags=[chunktag for (pos,chunktag) in tagged_pos_tags]
        conlltags=[(word,pos,chunktag) for ((word,pos),chunktag) in zip(sentence,chunktags)]
        return nltk.chunk.conlltags2tree(conlltags)
#构造相应的biggram模型
class BiggramChunker(nltk.ChunkParserI):
    def __init__(self,train_sents):
        train_data=[[(t,c) for w,t,c in nltk.chunk.tree2conlltags(sent)] for sent in train_sents]
        #对每一词进行词性标注然后进行分块
        self.tagger=nltk.BigramTagger(train_data)
    def parse(self,sentence):
        pos_tag=[pos for (word,pos) in sentence] #输入是[(),()]二元组数据结构
        tagged_pos_tags=self.tagger.tag(pos_tag)
        chunktags=[chunktag for (pos,chunktag) in tagged_pos_tags]
        conlltags=[(word,pos,chunktag) for ((word,pos),chunktag) in zip(sentence,chunktags)]
        return nltk.chunk.conlltags2tree(conlltags)
#test for the classifier of the training_data
# if __name__ == '__main__':
#     test_sents = conll2000.chunked_sents("test.txt", chunk_types=["NP"])
#     train_sents = conll2000.chunked_sents("train.txt", chunk_types=["NP"])
#     unigram_chunker = UnigramChunker(train_sents)
#     print(unigram_chunker.evaluate(test_sents))  # 方法来自继承父类的方法
#
#     biggram_chunker = BiggramChunker(train_sents)
#     print(biggram_chunker.evaluate(test_sents))
#
#     # 测试集
#     postags = sorted(set(pos for sent in train_sents for (word, pos) in sent.leaves()))
#     print(unigram_chunker.tagger.tag(postags))  # 使用词性tagger标注进行词块标注


#通过自定义的词性标注器，对相应的句子进行分块操作,连续词分类器
def npchunk_features(sentence,i,history):
    word,pos=sentence[i]
    return {"pos":pos}
def npchunk_features2(sentence,i,history):
    word,pos=sentence[i]
    if i==0:
        return {"pos":pos,"pre":"<START>"}
    else:
        word,pos=sentence[i-1]
        return {"pre_pos":pos,"pre_word":word}

class ConsecutiveNPChunkTagger(nltk.TaggerI):
    def __init__(self,train_sents):
        train_set=[]
        for tagged_sent in train_sents:
            untagged_sent=nltk.tag.untag(tagged_sent)
            history=[]
            for i,(word,tag) in enumerate(tagged_sent):
                featureset=npchunk_features(untagged_sent,i,history)
                train_set.append((featureset,tag))
                history.append(tag)
        self.classifier=nltk.MaxentClassifier.train(train_set,algorithm="megam",trace=0)
    def tag(self,sentence):
        history=[]
        for i in enumerate(sentence):
            featureset=npchunk_features(sentence,i,history)
            tag=self.classifier.classify(featureset)
            history.append(tag)
        return zip(sentence,history)

#构建基于自定义词性分类器的分块器
class ConsecutiveNPChunker(nltk.ChunkParserI):
    def __init__(self,train_sents):
        tagged_sents=[[((w,t),c) for t,w,c in nltk.chunk.tree2conlltags(sent)] for sent in train_sents]
        self.tagger=ConsecutiveNPChunkTagger(tagged_sents)
    def parse(self,sentence):
        tagged_sents=self.tagger.tag(sentence)
        conlltags=[(w,t,c) for ((w,t),c) in tagged_sents]
        return nltk.chunk.conlltags2tree(conlltags)
# if __name__ == '__main__':
#     test_sents = conll2000.chunked_sents("test.txt", chunk_types=["NP"])
#     train_sents = conll2000.chunked_sents("train.txt", chunk_types=["NP"])
#     chunker=ConsecutiveNPChunker(train_sents)
#     print(chunker.evaluate(test_sents))

# 命名实体：命名实体是指出现的人名，地名，以及日期等具有特定意义的名词，非常实用分类器进行建模识别分类
#nltk中提供了相应的训练好的包
sent=nltk.corpus.treebank.tagged_sents()[122]
print(nltk.ne_chunk(sent,binary=True)) #初次运行么有








