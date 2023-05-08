import re
import requests
import threading


# 爬取图片
def get_pic():
    r = requests.get('http://127.0.0.1:8000/')
    data = r.content.decode('utf-8')
    # html每一行都有"\n", 对html进行分割获得一个列表
    data = data.split('\n')
    # 创建一个列表存储所有图片的url地址(也就是图片网址)
    pic_url_list = []
    # 遍历data列表
    for row in data:
        # 通过正则解析出所有的图片url
        result = re.match(r'.*src="(.*)" width', row)  # <img src="./images/1.jpg" width="184px" height="122px" />
        if result:  # 解析出内容后将其存入列表
            pic_url_list.append(result.group(1))
    # 将图片保存到本地
    # 通过num给照片起名字 例如:0.jpg 1.jpg 2.jpg
    num = 0
    for pic_url in pic_url_list:
        # 通过requests.get()获取每一张图片
        r = requests.get('http://127.0.0.1:8000/' + pic_url[2:])
        # 保存每一张图片
        with open(f'images_save/{num}.jpg', 'wb') as f:
            f.write(r.content)
        # 文件名+1
        num += 1



def get_gdp():
    # 存储爬取到的国家的名字
    country_list = []
    # # 存储爬取到的gdp数据
    gdp_list = []
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
    pic_thread = threading.Thread(target=get_pic)
    gdp_thread = threading.Thread(target=get_gdp)

    pic_thread.start()
    gdp_thread.start()


