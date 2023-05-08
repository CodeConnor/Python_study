# GDP数据可视化格式 => [('美国',100亿),('中国',90亿),('日本',80亿)]
import re
import requests

# 存储爬取到的国家的名字
country_list = []
# # 存储爬取到的gdp数据
gdp_list = []

def get_gdp():
    # 获取html数据
    r = requests.get('http://127.0.0.1:8000/gdp.html')
    data = r.content.decode('utf-8')  # 数据解码
    data = data.split('\n')  # 分割数据

    # 遍历数据获取每行数据中的有效信息
    for row in data:
        # 使用正则解析数据获取国家名称
        result_country = re.match('.*<a href=""><font>(.*)</font>.*', row)
        if result_country:
            country_list.append(result_country.group(1))  # 将名称存入列表
        # 使用正则解析数据获取gdp数据
        result_gdp = re.match('.*￥(.*)亿元.*', row)
        if result_gdp:
            gdp_list.append(float(result_gdp.group(1)))  # 将数据存储为float类型

    # 组合列表
    country_gdp = list(zip(country_list, gdp_list))
    return country_gdp

if __name__ == '__main__':
    print(get_gdp())