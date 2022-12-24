import jieba # 分词
from PIL import Image # 图片处理
from matplotlib import pyplot as plt # 绘图数据可视化
from wordcloud import WordCloud # 词云
import numpy as np # 矩阵运算
import sqlite3

# 准备词云所需要的文字
conn = sqlite3.connect('movie250.db')
cur = conn.cursor()
sql = 'select introduction from movie250'
data = cur.execute(sql)
text = ''
for item in data :
    text = text + item[0] # 将所有文本拼接到一起
print(text)
cur.close()
conn.close()
# 分词
cut = jieba.cut(text)
string = ''.join(cut)
print(len(string))

img = Image.open(r'.\static\assets\img\tree.jpg') # 打开遮罩图片
img_array = np.array(img) # 将图片转变为图片数组
wc = WordCloud(
    background_color = 'white',# 形成词云图片背景
    mask = img_array, # 遮罩文件为数组
    font_path = 'msyhbd.ttc' ,# 字体 C:\Windows\Fonts\微软雅黑
)
wc.generate_from_text(string) # 从文本中选择生成的词云对象
# 绘制图片
fig = plt.figure(1) # 从第一个位置开始绘制
plt.imshow(wc) # 按照词云wc的规则进行显示词云图片
plt.axis('off') # 关闭坐标轴
# plt.show() # 查看效果
# 输出词云图片到文件
plt.savefig(r'.\static\assets\img\wordcloud.jpg',dpi = 500) # 分辨率500