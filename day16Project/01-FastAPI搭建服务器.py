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

# 启动服务器开始监听
uvicorn.run(app, host='127.0.0.1', port=8000)