import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 数据
data = {
    '桥名': ['武汉长江大桥', '武汉长江二桥', '白沙洲长江大桥', '军山长江大桥', '阳逻长江大桥',
            '天兴洲长江大桥', '二七长江大桥', '鹦鹉洲长江大桥', '沌口长江大桥', '杨泗港长江大桥', '青山长江大桥'],
    '通车类型': ['公铁两用，上层公路4车道，下层铁路双线', '城市快速路，双向六车道', '城市快速路，双向六车道',
                 '高速公路桥，双向六车道', '高速公路桥，双向6车道', '公铁两用，公路4车道，铁路4线',
                 '城市快速路，双向8车道', '城市快速路，双向8车道', '高速公路桥，双向八车道',
                 '城市快速路，双层公路桥，上层6车道，下层4车道及非机动车道、人行道', '高速公路桥，双向八车道'],
    '结构类型': ['钢桁架与钢筋混凝土结合', '双塔双索面钢筋混凝土斜拉桥', '双塔双索面栓焊结构钢箱梁与预应力混凝土箱梁组合的斜拉桥',
                 '半漂浮五跨连续双塔双索面钢箱梁斜拉桥', '一跨过江双塔单跨悬索桥型', '公铁两用斜拉桥',
                 '三塔斜拉桥，结合梁斜拉桥结构', '主缆连续的三塔四跨悬索桥', '五跨一联双塔双索面钢箱梁斜拉桥',
                 '双层悬索桥', '上承式钢拱桥'],
    '跨度（米）': ['主桥1156，总长1670', '主桥180 + 400 + 180，总长4407.6', '主桥50 + 180 + 618 + 180 + 50，总长3586.38',
                  '主桥964，全长4881.178', '主跨1280，全长约10000', '主桥4657，主跨504，公路引线8043，铁路引线60300',
                  '主桥2922，双主孔2×616，全长6507', '正桥3420，主跨850', '主桥1510，主跨760，全长8583',
                  '主跨1700，全长4134', '主跨938，全长7548'],
    '建成时间': ['1957年10月15日', '1995年6月9日', '2000年9月', '2001年12月15日', '2007年12月26日',
                 '2009年12月26日', '2011年12月31日', '2014年12月28日', '2017年12月28日', '2019年11月15日', '2017年12月28日']
}

df = pd.DataFrame(data)

# 设置seaborn风格
sns.set_style("whitegrid")

# 创建一个新的图形
plt.figure(figsize=(12, 8))

# 创建一个表格
table = plt.table(cellText=df.values,
                  colLabels=df.columns,
                  loc='center')

# 设置表格字体大小
table.auto_set_font_size(False)
table.set_fontsize(10)

# 调整表格行高
for i in range(len(df)):
    table._cells[(i + 1, 0)].set_height(0.1)

# 隐藏坐标轴
plt.axis('off')

# 显示图形
plt.show()