# 导入模块
from pyecharts.charts import Bar  # 按照需求导入模块，这里导入的是柱状图
from pyecharts import options as opts  # 导入图表项

# 创建实例化对象
# 链式操作：Bar().xxx.xxx.xxx
c = (
    Bar()
    .add_xaxis(['Apple', 'Redmi', 'Huawei', 'Lenovo'])
    .add_yaxis('商家A', [100, 200, 300, 50])
    .add_yaxis('商家B', [120, 220, 250, 100])
    .render('eg_bar.html')
)
