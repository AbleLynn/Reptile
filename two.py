# -*- codeing = utf-8 -*-
# @Time : 2021/9/26 11:39
# @Auther : AbleLynn
# @File : two.py
# @software : PyCharm



# import urllib.request
# from bs4 import BeautifulSoup
#
# url = 'http://book.zongheng.com/chapter/850594/56867918.html'      #以后只需改变地址和div即可
#
"""#获取指定网页链接中的文本内容"""
# def getContent(target):
#     response = urllib.request.urlopen(target)
#     html = response.read().decode('utf-8')
#
#     #开始分析网页
#     soup = BeautifulSoup(html,'html.parser')  #'html.parser'表示用parser解析器解析
#
#     content = soup.find_all(name='div',attrs={'itemprop':"acticleBody"})       #注意改变容器：div  容器名称：'itemprop':"acticleBody"
#     # content = soup.find("div", class_="title").text
#     # content = soup.find_all('div',itemprop="acticleBody",)
#     #注意以上三种方法的不同
#
#     content = content[0].text    #使用text属性，提取文本内容
#     content = content.replace('\xa0',' ').replace('   ','\n   ')   #替换原文汇总拉丁文编码
#     return content
#
# print(getContent(url))
#
#
"""# #多章节爬取文档  要使用前面单章节爬取的代码"""
#
# url = 'http://book.zongheng.com/showchapter/850594.html'       #目录页 即父页面
# #设置存放标题和网址的空列表
# novelTitle = []
# novelURL = []
#
# def getTarget(Directory):
#     response = urllib.request.urlopen(url)
#     html = response.read().decode('utf-8')
#
#     #解析页面
#     soup = BeautifulSoup(html,"html.parser")
#
#     list = soup.find_all(name = 'ul',attrs={'class':"chapter-list clearfix"})       #找到父页面的文本目录的容器
#     #匹配每一个<a>标签，并提取章节名和章节文章
#     list = BeautifulSoup(str(list[1]),"html.parser")    #首先解析取回页面的数据
#     #注意如果有名称相同的标签，则使用列表，选取自己想要爬取文本内容的容器，从0开始  str(list[1])
#     list = list.find_all('a')   #找<a>标签
#     for each in list:
#         # print(each.string,each.get('href'))     #打印章节名称，对应链接
#         novelTitle.append(each.string)      #将章节名称存入列表
#         novelURL.append(each.get('href'))   #将章节网址存入列表
#
# #一次打印各个章节内容
# getTarget(url)
#
# print('开始打印下载')
# for i in range(len(novelTitle)):
#     # print(novelTitle[i])
#     # print(getContent(novelURL[i]))
#     f = open("盖世小说.txt","a",encoding='utf-8')
#     f.write(novelTitle[i])
#     f.write(getContent(novelURL[i]))
# print('下载完成')





















