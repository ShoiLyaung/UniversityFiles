N=5000#处理数据量
import json
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib.font_manager import fontManager
import pyLDAvis
import pyLDAvis.gensim
import jieba.posseg as pseg
from snownlp import SnowNLP
from gensim import corpora, models, similarities
import os
import nltk
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re
   
# 读取数据
stop_words = set(nltk.corpus.stopwords.words('chinese'))
stop_words.add('不再')
stop_words.add('不想')
stop_words.add('永远')
# print(stop_words)
# 读取文本文件
with open('data/lyrics/music.json', 'r',encoding='utf-8') as file:
    json_data = file.read()

# 添加方括号并在每个JSON对象之间添加逗号
json_data = '[{}]'.format(json_data.replace('}\n{', '},\n{'))
# 解析JSON数据为Python对象
data = json.loads(json_data)
# 将Python对象转换为DataFrame
df = pd.DataFrame(data)
# 打印DataFrame
# print(df)

df['geci'] = df['geci'].astype(str)
# 判断歌词是否含有英文，并删除包含英文歌词的整行数据
df['contains_english'] = df['geci'].str.contains('[a-zA-Z]')
df = df[~df['contains_english']]
# 删除包含英文歌词的列
df = df.drop('contains_english', axis=1)

df['geci'] = df['geci'].str.replace("[\[\]']", "", regex=True)

data_needed = df['geci'][:N]
print(data_needed)

# data_needed=pd.read_csv("data/lyrics/lyrics.txt",sep="\n",header=None, encoding='utf-8')
# data_needed=data_needed[0][:N].tolist()
# print(data_needed)

print("数据读取完成")

# #情感分析
# sentiments = [SnowNLP(str(text)).sentiments for text in data_needed]
# sen_rec=[0,0,0]
# for sen in sentiments:
#     if sen >=0.6:
#         sen_rec[0]+=1
#     elif sen >=0.2:
#         sen_rec[1]+=1
#     else:
#         sen_rec[2]+=1
# index=["positive","neutral","negative"]
# bar=plt.bar(index,sen_rec,label='value',width=0.35)
# plt.rcParams['font.sans-serif']=['Microsoft YaHei']
# plt.bar_label(bar,label_type='edge')
# plt.title("音乐歌词情感分析")
# plt.savefig("Lyrics_sentiment.png",dpi=600)
# plt.close()

#分词
data_cut=[]
for item in data_needed:
    # print(item)
    tmp = pseg.cut(item)
    tmp2=[[word.word,word.flag] for word in tmp]
    data_cut.append(tmp2)

data_chosen1 = [[word[0] for word in text if word[1]=='n' 
         or word[1]=='v' or word[1]=='a' or word[1]=='d' or word[1]=='nr' 
         or word[1]=='nrfg' or word[1]=='ns' or word[1]=='nt' or word[1]=='nz' 
         or word[1]=='vn' or word[1]=='vd' or word[1]=='an' or word[1]=='ad' 
         or word[1]=='l'] for text in data_cut]

data_chosen2 = []
for text in data_chosen1:
    new_text = []
    for word in text:
        if word not in stop_words:
            new_text.append(word)
    data_chosen2.append(new_text)

data_chosen = [[word for word in text if len(word)>1]for text in data_chosen2]
print(data_chosen)

#聚类
texts = data_chosen

dictionary = corpora.Dictionary(texts) #构造词典
dictionary.filter_extremes(no_below=1, no_above=0.8)#去高频词

corpus = [dictionary.doc2bow(text) for text in texts] #构造语料库

lda = models.LdaModel(corpus, num_topics=10, id2word=dictionary, update_every=5, alpha=0.1, eta=0.1)

TopicWords = lda.show_topics(num_topics=10,num_words=20)

TopicWords[1][1].split('+')[1].split('*')

DocTopics = [ s for s in lda[corpus]]

DocTopics2 = []
for i in DocTopics:
    topics = [0,0,0,0,0,0,0,0,0,0]
    for j in i:
        topics[j[0]]=j[1]
    DocTopics2.append(topics)

topicID = []
weight = []
words = []
for word in TopicWords:
    for term in word[1].split('+'):
        topicID.append(word[0])
        weight.append(term.split('*')[0])
        words.append(term.split('*')[1])

data=pyLDAvis.gensim.prepare(lda, corpus, dictionary)
pyLDAvis.save_html(data,"static/Lyric.html")


#统计词频
from collections import defaultdict
dict = defaultdict(int)
for items in data_chosen:
    for item in items:
        dict[item]+=1
#绘制词云图
wordcloud = WordCloud(font_path="C:/Windows/Fonts/msyh.ttc",
                      background_color='white',
                      width=1080,height=720).generate_from_frequencies(dict)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis('off')
plt.savefig("static/images/Lyric_wordcloud.png",dpi=400)
plt.close()


terms = []
freq = []
for item in dict.items():
    terms.append(item[0])
    freq.append(item[1])

plt.rcParams['font.sans-serif']=['Microsoft YaHei']
term_needed = []
freq_needed = []
for i in range(10):
    rec_num=-1
    mem_word=''
    idx=-1
    for j in range(len(terms)):
        if freq[j]>rec_num:
            rec_num=freq[j]
            mem_word=terms[j]
            idx=j
    
    term_needed.append(mem_word)
    freq_needed.append(rec_num)
    del terms[idx]
    del freq[idx]

bar=plt.bar(term_needed,freq_needed,label='value')
plt.rcParams['font.sans-serif']=['Microsoft YaHei']
plt.bar_label(bar,label_type='edge')
plt.title("歌词最高词频统计")
plt.savefig("static/images/Lyrics_bar.png",dpi=600)
plt.close()

