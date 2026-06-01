# 爬取评论
# 使用import导入requests模块
import requests

# 从bs4中导入BeautifulSoup模块
from bs4 import BeautifulSoup

# 导入time模块
import time

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0',
           'Cookie':'bid=FmGO66DsV4o; ll="118281"; ap_v=0,6.0; __utma=30149280.1928264128.1780291679.1780291679.1780291679.1; __utmc=30149280; __utmz=30149280.1780291679.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmb=30149280.5.10.1780291679; __utma=223695111.863396862.1780291704.1780291704.1780291704.1; __utmb=223695111.0.10.1780291704; __utmc=223695111; __utmz=223695111.1780291704.1.1.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1780291704%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_id.100001.4cf6=e201f8f367f58a88.1780291704.; _pk_ses.100001.4cf6=1; _vwo_uuid_v2=D34BC7877AD5E767EBEA8D12BD54CE777|150ccdeccd5be0a93f009befd7e89433; dbcl2="157547797:ChhULinu6Bg"; ck=s3xA; frodotk_db="6a456be6a45c294f3ed043b3ed147bed"; push_noty_num=0; push_doumail_num=0'}

all_comments = []

for page in range(5):   # 爬5页
    start = page * 20

    url = f'https://movie.douban.com/subject/4922787/comments?status=P'

    print(f"正在爬第 {page+1} 页...")

    response = requests.get(url, headers=headers)
    response.encoding = response.apparent_encoding

    soup = BeautifulSoup(response.text, "lxml")

    content_all = soup.find_all(class_="comment-item")

    for comment in content_all:
        content_div = comment.find('span', class_='short')

        if content_div:
            data = content_div.get_text(strip=True)
            all_comments.append(data)   # 存起来
            print(data)

    time.sleep(2)  # 防止被封

print(f"\n一共爬取了 {len(all_comments)} 条评论")


# 把评论可视化为词云图


import jieba
from collections import Counter
from pyecharts.charts import WordCloud
from pyecharts import options as opts

# 合并所有评论文本
text = "".join(all_comments)

# 中文分词（非常关键）
words = jieba.lcut(text)

# 去除停用词（简单版）
stopwords = set([
    "的", "了", "是", "我", "也", "很", "都", "和", "就", "不", "人",
    "一个", "没有", "什么", "这个", "那个","甄嬛", "一个", "真的", "感觉",
    "可是","孙俪","后宫","觉得","已经","出去","PS","之前","之后","那么",
    "PK","76","但是","因为","关于"
])

filtered_words = [word for word in words if word not in stopwords and len(word) > 1]

# 统计词频
word_counts = Counter(filtered_words)

# 转成 pyecharts 需要的格式
data = list(word_counts.items())

# 生成词云
wc = (
    WordCloud()
    .add(
        series_name="评论词云",
        data_pair=data,
        word_size_range=[20, 100]
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="甄嬛传评论词云")
    )
)

# 输出为HTML文件
wc.render(r"C:\Users\Yaya\Desktop\词云图.html")


