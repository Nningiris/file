# 使用import导入requests模块
import requests

# 从bs4中导入BeautifulSoup模块
from bs4 import BeautifulSoup

# 使用import导入jieba模块
import jieba

# 从pyecharts.charts中导入WordCloud模块
from pyecharts.charts import WordCloud

# 导入time模块
import time

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'}


page = 20

for i in range(1,5):
    
    url = f'https://movie.douban.com/subject/4922787/comments?start={page}&limit=20&status=P&sort=new_score'

    # 将变量url作为参数，添加进requests.get()中，给赋值给response
    response = requests.get(url,headers = headers)

    # 调用.encoding属性获取requests模块的编码方式
    # 调用.apparent_encoding属性获取网页编码方式
    # 将网页编码方式赋值给response.encoding
    response.encoding = response.apparent_encoding

    # 将服务器响应内容转换为字符串形式，赋值给html
    html = response.text

    # 使用BeautifulSoup()读取html，添加lxml解析器，赋值给soup
    soup = BeautifulSoup(html,"lxml")

    # 使用find_all()查询soup中d的节点，赋值给content_all
    content_all = soup.find_all(class_ = "comment-item")

    # 循环多页
    page = page * i

    # 创建一个空白列表wordList
    wordList = []

    # for循环遍历content_all
    for comment in content_all:

        # 使用.string获取弹幕内容，并赋值给data
        data = comment.find(class_ = 'comment-content').span.text

        # 使用jieba.lcut()将data进行分词，赋值给words
        words = jieba.lcut(data)

        # 将列表wordList和列表words进行累加
        wordList = words + wordList

    # 创建一个空白字典wordDict
    wordDict = {}

    # for循环遍历列表wordList
    for word in wordList :
    
        # 如果列表中的元素长度大于1
        if len(word)>1 :
        
            # 如果该元素不存在字典的键中
            if word not in wordDict.keys():
            
                # 将字典中键所对应的值设置为1
                wordDict[word] = 1
        
            # 否则
            else :

                # 将字典中键所对应的值累加
                wordDict[word] = wordDict[word] + 1

# 创建WordCloud对象
wordCloud = WordCloud()

# 使用add()函数，series_name的值设置为空
# data_pair的值为字典wordDict转换成由元组组成的列表
# 将word_size_range的值设置为[20,80]
wordCloud.add(series_name = '',data_pair = wordDict.items(),word_size_range = [20,80])

# 使用wordCloud.render()存储文件，设置文件名为wordcloud.html
wordCloud.render(r'C:\Users\iriss\Desktop\wordcloud.html')

# 停顿两秒以防止网页反爬虫
time.sleep(2)

# 检查是否运行成功
print('success')