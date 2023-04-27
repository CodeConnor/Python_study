# 导入模块
from fastapi import FastAPI
from fastapi import Response
import uvicorn

# 创建FastAPI对象
app = FastAPI()


# 使用装饰器收发数据
@app.get('/index.html')
def main_page():
    with open('html/index.html', 'rb') as f:
        file_data = f.read()
    # 返回数据给客户端
    return Response(content=file_data, media_type='text/html')


# 启动服务
uvicorn.run(app, host='127.0.0.1', port=9090)
