# 导入模块
from fastapi import FastAPI
from fastapi import Response
import uvicorn

# 创建FastAPI对象
app = FastAPI()

# 使用装饰器收发信息
@app.get('/')  # 首页
def main():
    with open('source/html/index.html', 'rb') as f:
        data = f.read()
    # 返回数据给客户端
    return Response(content=data, media_type='text/html')

@app.get('/images/{path}')  # path 是一个路径参数，代表一个字符串变量，用于匹配 URL 中的路径
def get_pic(path: str):  # 接收图片通用配置
    with open(f'source/images/{path}', 'rb') as f:  # 响应数据到客户端，图片路径使用path
        data = f.read()

    return Response(content=data, media_type='jpg')

# 处理html请求
@app.get('/{path}')
def get_html(path: str):
    with open(f'source/html/{path}', 'rb') as f:
        data = f.read()

    return Response(content=data, media_type='text/html')

# 处理小图标请求
@app.get('/favicon.ico')
def get_ico():
    with open(f'source/html/favicon.ico', 'rb') as f:
        data = f.read()

    return Response(content=data, media_type='image/x-icon')

# 启动服务器开始监听
uvicorn.run(app, host='127.0.0.1', port=8000)
