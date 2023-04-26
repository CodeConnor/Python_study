import socket


if __name__ == '__main__':
    # 创建套接字对象
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口复用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 绑定端口
    tcp_server_socket.bind(('', 8000))
    # 设置监听
    tcp_server_socket.listen(128)

    while True:
        # 接收客户端连接
        new_socket, ip_port = tcp_server_socket.accept()
        # 接收客户端数据
        content = new_socket.recv(4096)
        print(content)