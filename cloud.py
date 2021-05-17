import jieba
import wordcloud
from PIL import Image
import numpy as np
#词云图制作

f=open('t6.txt','r',encoding='utf-8')
s=f.read()

strlist=jieba.lcut(s)
s=' '.join(strlist)
# print(s)

# mask = np.array(Image.open("mask.jpg"))
wc=wordcloud.WordCloud(font_path=r"d:/simfang_ttf/simfang.ttf", width=1900, height=900)
wc.generate(s)
wc.to_file('t6.png')