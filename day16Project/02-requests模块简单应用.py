# 导入模块
import requests

# 发起请求
res = requests.get('https://www.baidu.com/')

# 获取爬取的内容
data = res.content.decode('utf-8')
print(data)
