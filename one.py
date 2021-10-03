# -*- codeing = utf-8 -*-
# @Time : 2021/9/25 12:04
# @Auther : AbleLynn
# @File : one.py
# @software : PyCharm

#网页静态数据爬取

# import urllib.request
# from bs4 import BeautifulSoup   #上面两个库用于爬取
# from wordcloud import WordCloud    #制作词云
# from wordcloud import STOPWORDS    #采用停用文本去除常用词汇
# import matplotlib.pyplot as plt
# from imageio import imread     #词云图片格式设置
# import jieba
# import operator
#
#
"""# #爬取网页HTML文件"""
# response = urllib.request.urlopen('http://www.gov.cn/guowuyuan/zfgzbg.htm')  #urlopen:获取页面
# html = response.read().decode('utf-8') #read():读取HTTPResponse类型数据   decode():按照指定的编码格式解码字符串
#
# #筛选政府工作报告正文
# soup = BeautifulSoup(html,"html.parser") #HTML文件解析
# content = soup.find("div",class_="conlun2_box_text").text
#
# # 以"W"的方式打开一个文件，若原来没有该文件，则新建一个
# file = open("政府工作报告.txt","w")
# file.write(content)
# file.close()
#
# #打印抓去的text
# # print(content)
#
# # #词云：是对网络文本中出现频率较高的”关键词“给予视觉上的突出，形成“关键词云层”或“关键词渲染”，从而过滤大量无意义的信息，突出文章或者网页内容的主旨
# # im = imread('heart.jpg')   #读取选中图片  N
# # w = WordCloud(mask = im)   #将词云图片仿照选中图片显示样式 N
# # w = WordCloud(width = 1000, height = 800)   #设置词云生成图片的高度宽度  N
# # w = WordCloud(background_color="white")   #设置词云生成的背景颜色  N
# # w = WordCloud(stopwords = STOPWORDS.add("一带一路"))  #指定词云的排除词列表，即不显示的单词列表
# w = WordCloud(font_path="/Fonts/simhei.ttf").generate(content)  #生成词云   font_path  指定文体中的路径，默认为None
#                                                                 # "/Fonts/simhei.ttf"为设置中文字体 因为wordcloud不能识别中文
# # w = WordCloud().generate(content)
# w.to_file("政府工作报告V1.png")  #保存词云图片
# plt.imshow(w)  #对图像进行处理，并显示其格式
# plt.axis('off')   #隐藏词云图片的坐标轴边界
# plt.show()   #显示处理后的词云图片
#
# #词频统计
#
# # #去除特殊符号
# # for ch in '|"#$%&()+,-./:;<=>?@[\\]^{|}~':
# #     txt = txt.replace(ch,"")
#
# #文本分词 将文本拆成单独的词
#
# #step1读取文件内容
# fileContent = open('政府工作报告.txt','r').read()
#
# #step2去除特殊字符
# for ch in '|"#$%&()+,-./:;<=>?@[\\]^{|}~，。（）、：《》！“”':  #也可以将特殊字符加入到停用字符库中使用，即可以省略这一步
#     fileContent = fileContent.replace(ch,"")
#
# #step3文本分词 利用jieba库进行分词
# words = jieba.cut(fileContent)
# #去除停用词，stopwords_CN为事先保存的停用词文件
# stopwords = []
# with open('stopwords_CN.txt','r',encoding='utf-8') as f:
#     stopwords = f.read()
# #利用空格分隔每个词，查看分词结果
# # for word in words:
# #     print(word,end=' ')
#
# #一、step4开始中文词频统计
# counts = {}
# #若单词在文章中，返回该单词对应的个数并+1
# #若单词不在文章中，则返回这个单词加到字典中并返回0再+1
# for word in words:
#     if word not in stopwords: #不是停用词才统计词频
#         counts[word] = counts.get(word,0) + 1
# # print(counts)
#
# #step5 词频排序
# items = list(counts.items())  #将字典转换为列表
# # items.sort()  #直接排序
# # print(items)
#
# #利用sort()方法根据词频进行排序
# # list.sort(key = None, reverse = False)
# #第一种
# items.sort(key= lambda x:x[1], reverse= True)
# # #第二种 使用operator库中的itemgetter()根据词频进行排序
# # items.sort(key= operator.itemgetter(1), reverse= True)
# # print(items)
#
# #按词频由高到低输出TOP20高频词汇
# wordStr = ''
# for i in range(20):
#     word,count = items[i]
#     print("{0:<10}{1:>5}".format(word,count))
#     wordStr += ' ' + word  #使用空格分隔每个词汇
#
# # #词云检测
# # w = WordCloud(font_path="/Fonts/simhei.ttf").generate(wordStr)
# # w.to_file("政府工作报告V2.png")  #保存词云图片
# # plt.imshow(w)  #对图像进行处理，并显示其格式
# # plt.axis('off')   #隐藏词云图片的坐标轴边界
# # plt.show()   #显示处理后的词云图片
#
# #词云检测终极图
# w = WordCloud(font_path="/Fonts/simhei.ttf")
# w = w.fit_words(wordStr)
# w.to_file("政府工作报告V3.png")  #保存词云图片
# plt.imshow(w)  #对图像进行处理，并显示其格式
# plt.axis('off')   #隐藏词云图片的坐标轴边界
# plt.show()   #显示处理后的词云图片


# #二、step4开始英文词频统计
# #英文分词
# # txt.split()：按照指定分隔符对字符串进行切片，默认为空格
# # 统一转换为小写字母：txt.lower()
# # 统一转换为大写字母：txt.upper()
#
# #step1 读取文件
# file = open("The Autumn After Next.txt","r",encoding='utf-8')
#
# #step2 文件预处理
# txt = file.read().lower()  #读取文件，并将字母转换为小写
# for ch in '|"#$%&()+,-./:;<=>?@[\\]^{|}~':
#     txt = txt.replace(ch,'')  #用空格代替特殊字符
#
# #step3 文本分词
# words = txt.split() #默认用空格分离并以列表形式返回
# # print(words)
#
# #step4取出停用词备用
# stopwords = []
# with open('stopwords_ENG.txt') as f:
#     stopwords = f.read()
#
# #开始词频统计
# counts = {}
# for word in words:
#     if word not in stopwords:
#         counts[word] = counts.get(word,0) + 1
# #将字典转换成列表
# items = list(counts.items())
#
# #按列表元素中的第二个项从大到小排列
# items.sort(key= lambda x:x[1],reverse=True)
#
# #输出，控制格式
# wordStr = ''
# for i in range(20):
#     word,count = items[i]
#     print("{0:<10}{1:>5}".format(word,count))
#     # wordList.append(word)
#     wordStr += ' ' + word  #用空格连接每一个词
#
# #词云检测
# w = WordCloud().generate(wordStr) #生成词云
# w.to_file("The Autumn After Next.png")  #保存词云图片
# plt.imshow(w)  #对图像进行处理，并显示其格式
# plt.axis('off')   #隐藏词云图片的坐标轴边界
# plt.show()   #显示处理后的词云图片













