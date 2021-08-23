import jieba
from os import path
from imageio import imread
import matplotlib.pyplot as plt
import os
from wordcloud import WordCloud, ImageColorGenerator

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = os.getcwd()

stopwords_path = d + '/wc_cn/stopwords_cn_en.txt'
# Chinese fonts must be set
font_path = d + '/fonts/SourceHanSerif/SourceHanSerifK-Light.otf'

# the path to save worldcloud
imgname1 = d + '/LuXun.jpg'
imgname2 = d + '/LuXun_colored.jpg'
# read the mask / color image taken from
back_coloring = imread(path.join(d,'1.png'))

# Read the whole text.
# text = open(path.join(d, d + '/wc_cn/CalltoArms.txt')).read()
text = '''今晚的满月会伴随一场月全食上演，而且还是一场“超级月全食”。

什么是月全食呢？胡方浩介绍，当月亮、地球、太阳完全在一条直线上的时候，整个月亮全部走进地球的影子里，月亮表面昏暗，月全食就形成了。

今晚的月全食过程中，月球穿过地影的距离短，导致全食持续时间也较短。从食既到生光只有短短的20分钟。

月全食的过程分为初亏、食既、食甚、生光、复圆五个阶段。

初亏：月球刚接触地球本影，标志月食开始

食既：月球的西边缘与地球本影的西边缘内切，月球刚好全部进入地球本影内

食甚：月球的中心与地球本影的中心最近

生光：月球东边缘与地球本影东边缘相内切，这时全食阶段结束

复圆：月球的西边缘与地球本影东边缘相外切，这时月食全过程结束

根据紫金山天文台预报，本次月全食（红月亮）：初亏17时45分；食既19时09分；食甚19时19分，最大食分1.015；生光19时28分；复圆20时53分。当天，我国部分城市的月出时间是（按先后排列）：台北18时31分，上海18时44分，南京18时57分，深圳18时58分，青岛19时00分，广州19时02分，哈尔滨19时04分，北京19时27分。

我国除西藏西部、新疆西部以外的地区都可见带食而出，越往东的地区看到的月食越完整，月食持续的时间也越长。
'''


# The function for processing text with Jieba
def jieba_processing_txt(text):
    mywordlist = []
    seg_list = jieba.cut(text, cut_all=False)
    liststr = "/ ".join(seg_list)

    with open('stopwords.txt', encoding='utf-8') as f_stop:
        f_stop_text = f_stop.read()
        f_stop_seg_list = f_stop_text.splitlines()

    for myword in liststr.split('/'):
        if not (myword.strip() in f_stop_seg_list) and len(myword.strip()) > 1:
            mywordlist.append(myword)
    return ' '.join(mywordlist)


wc = WordCloud(font_path='msyh.ttc', background_color="white", max_words=2000, mask=back_coloring,
               max_font_size=100, random_state=42, width=1000, height=860, margin=2,)

print(jieba_processing_txt(text))
wc.generate(jieba_processing_txt(text))

# create coloring from image
image_colors_default = ImageColorGenerator(back_coloring)

plt.figure()
# recolor wordcloud and show
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()

# save wordcloud
wc.to_file(path.join(d, imgname1))

# create coloring from image
image_colors_byImg = ImageColorGenerator(back_coloring)

# show
# we could also give color_func=image_colors directly in the constructor
plt.imshow(wc.recolor(color_func=image_colors_byImg), interpolation="bilinear")
plt.axis("off")
plt.figure()
plt.imshow(back_coloring, interpolation="bilinear")
plt.axis("off")
plt.show()

# save wordcloud

wc.to_file(path.join(d, imgname2))