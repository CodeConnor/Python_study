import re
import requests

# 获取图片的url地址
def get_pic_url():
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
    return pic_url_list

# 将图片保存到本地
def save_pic(pic_url_list):
    # 通过num给照片起名字 例如:0.jpg 1.jpg 2.jpg
    num = 0
    for pic_url in pic_url_list:
        # 通过requests.get()获取每一张图片
        r = requests.get('http://127.0.0.1:8000/' + pic_url[2:])
        # 保存每一张图片
        with open(f'images_save/{num}.jpg', 'wb') as f:
            f.write(r.content)

        num += 1

if __name__ == '__main__':
    pic_url_list = get_pic_url()
    save_pic(pic_url_list)
