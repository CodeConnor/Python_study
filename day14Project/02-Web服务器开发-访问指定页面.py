import socket

if __name__ == '__main__':
    # 创建套接字对象
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口复用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 绑定端口
    tcp_server_socket.bind(('', 9000))
    # 设置监听
    tcp_server_socket.listen(128)

    while True:
        # 接收客户端连接
        new_socket, ip_port = tcp_server_socket.accept()
        # 接收客户端数据
        client_data = new_socket.recv(4096)
        if client_data:
            # 对客户端请求解码
            client_data = client_data.decode('utf-8')
            # 切片, 获取页面信息和路径
            request_data = client_data.split(' ', maxsplit=2)
            request_path = request_data[1]
            # 如何用户没有指定访问具体页面，则默认访问首页
            if request_path == '/':
                request_path = '/index.html'
            # 响应数据到客户端
            with open('html' + request_path, 'rb') as f:  # 读取html文件，使用 rb 模式是因为需要读音频视频文件等
                html_data = f.read()

            # 关键点：将以上数据拼接为HTTP响应报文
            response_line = 'HTTP/1.1 200 OK\r\n'  # 响应行
            response_header = 'Server:PWB/1.1\r\n'  # 响应头
            # 空行 => \r\n => 写在拼接中
            response_body = html_data  # 响应体
            # 拼接，将字符串拼接然后编码为二进制数据，响应体不用编码，因为rb模式读出的数据即为二进制数据
            response_data = (response_line + response_header + '\r\n').encode('utf-8') + response_body
            new_socket.send(response_data)
            # 关闭套接字
            new_socket.close()