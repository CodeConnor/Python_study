# 导入模块
from fastapi import FastAPI
from fastapi import Response
import uvicorn
import logging



# 输出日志信息到文件
f = open('fastapi.log', 'a', encoding='utf-8')  # 创建文件保存日志信息
# 调整日志输出的最低等级和日志格式
# 格式：2023-05-09 10:17:37,066 - 10-logging日志信息.py[line:9] - root - DEBUG: 这是一条debug级别日志信息！
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(name)s - %(levelname)s: %(message)s',
                    # 输出日志到文件中
                    stream=f
                    )

# 创建FastAPI对象
app = FastAPI()


# 使用装饰器收发信息
@app.get('/')  # 首页
def main():
    with open('source/html/index.html', 'rb') as f:
        data = f.read()
    logging.info('访问了/首页')  # 记录日志
    # 返回数据给客户端
    return Response(content=data, media_type='text/html')


@app.get('/images/{path}')  # path 是一个路径参数，代表一个字符串变量，用于匹配 URL 中的路径
def get_pic(path: str):  # 接收图片通用配置
    with open(f'source/images/{path}', 'rb') as f:  # 响应数据到客户端，图片路径使用path
        data = f.read()
    logging.info(f'访问了/images/{path}图片')
    return Response(content=data, media_type='jpg')


# 处理html请求
@app.get('/{path}')
def get_html(path: str):
    with open(f'source/html/{path}', 'rb') as f:
        data = f.read()
    logging.info(f'访问了/{path}文件')
    return Response(content=data, media_type='text/html')


# 处理小图标请求
@app.get('/favicon.ico')
def get_ico():
    with open(f'source/html/favicon.ico', 'rb') as f:
        data = f.read()
    logging.info('访问了/favicon.ico小图标')
    return Response(content=data, media_type='image/x-icon')


# 启动服务器开始监听
uvicorn.run(app, host='127.0.0.1', port=8000)
