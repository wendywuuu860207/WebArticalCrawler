#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import urllib
import re
from bs4 import BeautifulSoup as bs
from nltk.tokenize import word_tokenize
from nltk.book import *
from nltk import bigrams
from nltk import trigrams

#the url to scrap the article；抓取網頁程式碼
URL = "https://en.wikipedia.org/wiki/Duck"
response = urllib.request.urlopen(URL)
html_cont =  response.read()
soup = bs(html_cont, 'html.parser', from_encoding='utf-8')
#remove html code and remain only string；將網頁資料丟給BS4組合成純文字文章，並清除超連結
paragraphs = soup.find_all('p')
text = ""
for p in paragraphs:
    for i in p.find_all('sup'):
        i.clear()
    text += p.text

#use nltk to split the article to words；將文章切成單字
text_tokens = nltk.word_tokenize(text)
#remove symbol；去除標點符號
english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%', '``', "''" ]
text_tokens = [word for word in text_tokens if word not in english_punctuations]
#use nltk to tag the word's parts of speech；將切好的單字進行詞性標記
text_tagged = nltk.pos_tag(text_tokens)
#sort the text_tagged list by the tag of the item；詞性頻率計算並印出最常出現的五種詞性
freqtg = [tag for (word, tag) in text_tagged]
fdt = nltk.FreqDist(freqtg).most_common(5)
print("The five most frequently occurring parts of speech:")
print(fdt)
print("\n")


#去除大小寫後最常出現的五個單字
#let all the word be lower；將大寫字母轉為小寫
paragraphLow = text.lower()
text_tokens_low = nltk.word_tokenize(paragraphLow)
#remove symbol；去除標點符號
text_tokens_low = [word for word in text_tokens_low if word not in english_punctuations]
freqLow = nltk.FreqDist(text_tokens_low)
print("The five most common words(whihout capital):")
print(freqLow.most_common(5))
print("\n")

#split the article to sentences斷句
sen_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
sentences = sen_tokenizer.tokenize(text)
#bigram & trigram
count = 0
bilist = []
trilist = []
for s in sentences:
    sentence_words = nltk.word_tokenize(sentences[count])
    #remove symbol；去除標點符號 
    sentence_words = [word for word in sentence_words if word not in english_punctuations]
    bb = bigrams(sentence_words)
    tt = trigrams(sentence_words)
    bilist.extend(bb)
    trilist.extend(tt)
    count+=1
    
#the five most common digram  
#biD = nltk.FreqDist(bilist).most_common(5)
#the five most common trigram  
#triD = nltk.FreqDist(trilist).most_common(5)

#print result of max digram and trigram
print("The most common digram:")
print(nltk.FreqDist(bilist).most_common(1))
print("\n")
print("The most common trigram:")
print(nltk.FreqDist(trilist).most_common(1))
print("\n")
