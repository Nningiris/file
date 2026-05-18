# 从pyecharts库中导入Graph
from pyecharts.charts import Graph

# 从pyecharts库中导入options并简写为opts
from pyecharts import options as opts

# 创建对象赋值给graph
graph = Graph()

# 存储类别的列表category
category = [{'name':'甄嬛战队'},{'name':'皇后战队'},{'name':'华妃战队'},{'name':'太后战队'},{'name':'皇帝战队'},{'name':'中立派'}]

# 存储主要人物关系的列表info 
info = [
    {"id": "甄嬛", "name": "甄嬛",'category':0, 'symbolSize':60},
    {"id": "皇后", "name": "皇后（乌拉那拉.宜修）",'category':1, 'symbolSize':40},
    {"id": "江福海", "name": "江福海（皇后的太监）",'category':1, 'symbolSize':10},
    {"id": "剪秋", "name": "剪秋（皇后侍女）",'category':1, 'symbolSize':10},
    {"id": "大阿哥", "name": "大阿哥弘晖（皇后之子 夭折）",'category':1, 'symbolSize':10},
    {"id": "纯元皇后", "name": "纯元皇后（皇后的姐姐 已逝）",'category':4, 'symbolSize':10},
    {"id": "皇帝", "name": "雍正帝",'category':4, 'symbolSize':50},
    {"id": "苏培盛", "name": "苏培盛（太监首领）",'category':4, 'symbolSize':10},
    {"id": "小夏子", "name": "小夏子（苏培盛徒弟）",'category':4, 'symbolSize':10},
    {"id": "芳若", "name": "芳若（御前侍女）",'category':4, 'symbolSize':10},
    {"id": "果郡王", "name": "果郡王（允礼 排名十七）",'category':0, 'symbolSize':10},
    {"id": "太后", "name": "太后（乌雅.成璧）",'category':3, 'symbolSize':20},
    {"id": "竹息", "name": "竹息（太后侍女）",'category':3, 'symbolSize':10},
    {"id": "隆科多", "name": "隆科多（太后老情人）",'category':3, 'symbolSize':10},
    {"id": "沈眉庄", "name": "沈眉庄",'category':0, 'symbolSize':10},
    {"id": "温实初", "name": "温实初 （沈眉庄爱人）",'category':0, 'symbolSize':10},
    {"id": "安陵容", "name": "安陵容",'category':1, 'symbolSize':10},
    {"id": "宝娟", "name": "宝娟（安陵容侍女）",'category':1, 'symbolSize':10},
    {"id": "敬妃", "name": "敬妃",'category':0, 'symbolSize':10},
    {"id": "华妃", "name": "华妃（年世兰）",'category':2, 'symbolSize':30},
    {"id": "年羹尧", "name": "年羹尧（华妃哥哥）",'category':2, 'symbolSize':10},
    {"id": "周宁海", "name": "周宁海（华妃的太监）",'category':2, 'symbolSize':10},
    {"id": "黄规全", "name": "黄规全（内务府总管 华妃远亲）",'category':2, 'symbolSize':10},
    {"id": "端妃", "name": "端妃",'category':4, 'symbolSize':10},
    {"id": "吉祥", "name": "吉祥（端妃侍女）",'category':4, 'symbolSize':10},
    {"id": "丽嫔", "name": "丽嫔",'category':2, 'symbolSize':10},
    {"id": "欣贵人", "name": "欣贵人",'category':5, 'symbolSize':10},
    {"id": "齐妃", "name": "齐妃",'category':1, 'symbolSize':10},
    {"id": "翠果", "name": "翠果（齐妃侍女）",'category':1, 'symbolSize':10},
    {"id": "三阿哥", "name": "三阿哥弘时（齐妃之子）",'category':1, 'symbolSize':10},
    {"id": "四阿哥", "name": "四阿哥弘历（皇帝私生子 下一任皇帝）",'category':0, 'symbolSize':10},
    {"id": "曹贵人", "name": "曹贵人",'category':2, 'symbolSize':10},
    {"id": "祺贵人", "name": "祺贵人（瓜尔佳.文鸳）",'category':1, 'symbolSize':10},
    {"id": "瓜尔佳.鄂敏", "name": "瓜尔佳.鄂敏（祺贵人之父）",'category':2, 'symbolSize':10},
    {"id": "舒太妃", "name": "舒太妃（果郡王之母）",'category':5, 'symbolSize':10},
    {"id": "孟静娴", "name": "孟静娴（沛国公之女）",'category':5, 'symbolSize':10},
    {"id": "淳常在", "name": "淳常在",'category':0, 'symbolSize':10},
    {"id": "富察贵人", "name": "富察贵人",'category':1, 'symbolSize':10},
    {"id": "颂芝", "name": "颂芝（华妃丫鬟）",'category':2, 'symbolSize':10},
    {"id": "甄玉娆", "name": "甄玉娆（甄嬛妹妹）",'category':0, 'symbolSize':10},
    {"id": "叶澜依", "name": "宁嫔（叶澜依）",'category':0, 'symbolSize':10},
    {"id": "瑛贵人", "name": "瑛贵人",'category':5, 'symbolSize':10},
    {"id": "夏冬春", "name": "夏常在（夏冬春）",'category':1, 'symbolSize':10},
    {"id": "余莺儿", "name": "余答应（余莺儿）",'category':1, 'symbolSize':10},
    {"id": "浣碧", "name": "浣碧/甄玉隐（甄嬛侍女/妹妹）",'category':0, 'symbolSize':10},
    {"id": "流珠", "name": "流珠（甄嬛侍女）",'category':0, 'symbolSize':10},
    {"id": "瑾汐", "name": "瑾汐（甄嬛侍女）",'category':0, 'symbolSize':10},
    {"id": "小允子", "name": "小允子（甄嬛的太监）",'category':0, 'symbolSize':10},
    {"id": "温宜", "name": "温宜公主（曹贵人之女）",'category':0, 'symbolSize':10},
    {"id": "胧月", "name": "胧月公主（甄嬛大女）",'category':0, 'symbolSize':10},
    {"id": "静和", "name": "静和公主（沈眉庄之女）",'category':0, 'symbolSize':10},
    {"id": "六阿哥", "name": "六阿哥弘曕（甄嬛之子）",'category':0, 'symbolSize':10},
    {"id": "灵犀", "name": "灵犀公主（甄嬛次女）",'category':0, 'symbolSize':10},
    {"id": "慎贝勒", "name": "慎贝勒（允禧 皇帝弟弟）",'category':5, 'symbolSize':10},
    {"id": "甄远道", "name": "甄远道（甄嬛父亲）",'category':0, 'symbolSize':10},
]

# 存储人物间关系的列表coo
coo =  [ {"source":"皇帝", "target":"甄嬛"},
         {"source":"皇帝", "target":"皇后"},
         {"source":"皇帝", "target":"端妃"},
         {"source":"皇帝", "target":"纯元皇后"},
         {"source":"皇帝", "target":"太后"},
         {"source":"皇帝", "target":"华妃"},
         {"source":"皇帝", "target":"果郡王"},
         {"source":"皇帝", "target":"慎贝勒"},
         {"source":"皇帝", "target":"年羹尧"},
         {"source":"皇帝", "target":"甄远道"},
         {"source":"皇帝", "target":"苏培盛"},
         {"source":"皇帝", "target":"芳若"},
         {"source":"皇帝", "target":"瓜尔佳.鄂敏"},
         {"source":"皇帝", "target":"年羹尧"},
         {"source":"皇帝", "target":"颂芝"},
         {"source":"皇帝", "target":"小夏子"},
         {"source":"皇帝", "target":"四阿哥"},
         {"source":"皇帝", "target":"余莺儿"},
         {"source":"甄嬛", "target":"沈眉庄"},
         {"source":"甄嬛", "target":"流珠"},
         {"source":"甄嬛", "target":"瑾汐"},
         {"source":"甄嬛", "target":"小允子"},
         {"source":"甄嬛", "target":"敬妃"},
         {"source":"甄嬛", "target":"胧月"},
         {"source":"甄嬛", "target":"六阿哥"},
         {"source":"甄嬛", "target":"灵犀"},
         {"source":"甄嬛", "target":"甄远道"},
         {"source":"甄嬛", "target":"浣碧"},
         {"source":"甄嬛", "target":"甄玉娆"},
         {"source":"甄嬛", "target":"淳常在"},
         {"source":"甄嬛", "target":"叶澜依"},
         {"source":"甄嬛", "target":"四阿哥"},
         {"source":"甄嬛", "target":"四阿哥"},
         {"source":"甄嬛", "target":"欣贵人"},
         {"source":"甄嬛", "target":"安陵容"},
         {"source":"甄嬛", "target":"果郡王"},
         {"source":"甄嬛", "target":"温实初"},
         {"source":"甄嬛", "target":"苏培盛"},
         {"source":"甄嬛", "target":"静和"},
         {"source":"瑾汐", "target":"苏培盛"},
         {"source":"苏培盛", "target":"小夏子"},
         {"source":"果郡王", "target":"浣碧"},
         {"source":"果郡王", "target":"孟静娴"},
         {"source":"果郡王", "target":"舒太妃"},
         {"source":"果郡王", "target":"叶澜依"},
         {"source":"皇后", "target":"齐妃"},
         {"source":"皇后", "target":"安陵容"},
         {"source":"皇后", "target":"剪秋"},
         {"source":"皇后", "target":"江福海"},
         {"source":"皇后", "target":"祺贵人"},
         {"source":"皇后", "target":"富察贵人"},
         {"source":"皇后", "target":"大阿哥"},
         {"source":"皇后", "target":"夏冬春"},
         {"source":"皇后", "target":"余莺儿"},
         {"source":"皇后", "target":"纯元皇后"},
         {"source":"皇后", "target":"瓜尔佳.鄂敏"},
         {"source":"华妃", "target":"颂芝"},
         {"source":"华妃", "target":"曹贵人"},
         {"source":"华妃", "target":"丽嫔",},
         {"source":"华妃", "target":"黄规全"},
         {"source":"华妃", "target":"周宁海"},
         {"source":"华妃", "target":"年羹尧"},
         {"source":"太后", "target":"竹息"},
         {"source":"太后", "target":"皇后"},
         {"source":"太后", "target":"隆科多"},
         {"source":"慎贝勒", "target":"甄玉娆"},
         {"source":"端妃", "target":"吉祥"},
         {"source":"端妃", "target":"温宜"},
         {"source":"敬妃", "target":"胧月"},
         {"source":"齐妃", "target":"翠果"},
         {"source":"沈眉庄", "target":"温实初"},
         {"source":"沈眉庄", "target":"静和"},
         {"source":"祺贵人", "target":"瓜尔佳.鄂敏"},
         {"source":"安陵容", "target":"宝娟"},
         {"source":"曹贵人", "target":"温宜"},
         {"source":"齐妃", "target":"三阿哥"},
         {"source":"浣碧", "target":"瑛贵人"},
         {"source":"瑛贵人", "target":"三阿哥"},
         {"source":"祺贵人", "target":"瓜尔佳.鄂敏"},
        ]

# 使用Graph()函数创建对象赋值给graph
graph = Graph()

# 设置画布大小为宽度1200像素，高度1000像素
graph = Graph(init_opts=opts.InitOpts(width="1400px", height="800px"))

# 设置全局变量
# 设置关系图标题，位置及字号
graph.set_global_opts(
    title_opts=opts.TitleOpts(
        title='甄嬛传人物关系图', # 设置关系图标题
        pos_top='top',           # 标题置于画布顶部
        pos_left='center',        # 标题置于正中间
        title_textstyle_opts=opts.TextStyleOpts(
            font_size=20         # 调整标题字号
        )
    ),
    legend_opts=opts.LegendOpts(
        orient = 'vertical',  # 垂直显示图例
        pos_left = '3%',  # 调整图例在距离画布左边界3%的位置
        pos_top = '40%'  # 调整图例在距离画布上边界40%的位置
    )
)

# 调用add()函数，设置series_name为空
# 将info赋值给nodes，将coo赋值给links
graph.add(
    series_name="",
    nodes=info,
    links=coo,
    layout = 'circular',
    is_rotate_label = True,
    linestyle_opts = opts.LineStyleOpts(color = 'source',curve = 0.3),
    categories = category
)

# 使用render()生成文件存储
graph.render(r"C:\Users\Yaya\Desktop\甄嬛传人物关系图.html")

