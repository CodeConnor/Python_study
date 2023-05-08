from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType

c = (
    Bar(init_opts=opts.InitOpts(width='1500px', height='800px', theme=ThemeType.ROMANTIC)
        )
    .add_xaxis(Faker.choose())
    .add_yaxis('商家A', Faker.values())
    .add_yaxis('商家B', Faker.values())
    .set_global_opts(title_opts=opts.TitleOpts(title='JD商家A与商家B销售量对比图'),
                     legend_opts=opts.LegendOpts(pos_left=665, pos_top=10),
                     visualmap_opts=opts.VisualMapOpts(is_show=True)
                     )
    .render('eg_opts.html')
)
