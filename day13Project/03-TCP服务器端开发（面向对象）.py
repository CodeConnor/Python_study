import socket
# 创建服务器端类
class WebServer(object):
    # 初始化服务器属性：1、创建套接字对象 2、绑定IP和端口 3、监听客户端
    def __init__(self):
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server_socket.bind(('', 8000))  # ip为空时，默认使用本机地址
        self.tcp_server_socket.listen(128)

    # 定义start方法，接收客户端连接
    # 允许多个客户端连接，但每次只能有一个客户端向服务器发送信息（单线程）
    def start(self):
        while True:  # 通过循环实现持续接收客户端信息
            new_socket, ip_port = self.tcp_server_socket.accept()  # accept可以阻塞程序执行，相当于input
            content = new_socket.recv(1024).decode('gbk')
            print(f'客户端地址：{ip_port}\n客户端发送信息：{content}')
            new_socket.send('信息已收到，over！'.encode('gbk'))
            new_socket.close()

# 实例化服务器端
ws = WebServer()
# 开始接收
ws.start()
