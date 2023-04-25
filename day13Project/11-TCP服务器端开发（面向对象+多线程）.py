import socket
import threading

class WebServer(object):
    # 定义方法，初始化套接字对象
    def __init__(self):
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 1、创建套接字对象
        # 设置端口复用，让服务器端占用的端口在执行结束可以立即释放，不影响后续程序的使用
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        self.tcp_server_socket.bind(('', 8000))  # 2、绑定ip和端口
        self.tcp_server_socket.listen(128)  # 3、监听client

    # 定义方法，接收、发送信息
    def handle_request(self, new_socket, ip_port):
        # 5、接收信息
        content = new_socket.recv(1024).decode('gbk')
        print(f'{ip_port}: {content}')
        # 6、回复信息
        new_socket.send('Received, over!'.encode('gbk'))
        # 7、关闭套接字对象
        new_socket.close()

    # 定义方法，接收客户端连接
    def start(self):
        # 4、使用循环不断接收客户端请求
        while True:
            new_socket, ip_port = self.tcp_server_socket.accept()
            # 4.1 创建线程
            request_thread = threading.Thread(target=self.handle_request, args=(new_socket, ip_port))
            # 4.2 启动线程
            request_thread.start()


# 程序入口
if __name__ == '__main__':
    # 实例化
    ws = WebServer()
    ws.start()
