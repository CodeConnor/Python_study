# TCP客户端开发
# 导入socket模块
import socket

# 1、创建客户端套接字对象
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # family为AF_INET(ipv4)，type为SOCK_STREAM(TCP)
# 2、创建连接
tcp_client_socket.connect(('127.0.0.1', 8000))  # 使用元组保存服务器地址和端口
# 3、发送数据到服务器端
tcp_client_socket.send('I love Python!'.encode('gbk'))  # 数据编码方式为gbk
# 4、接收服务器端返回的应答数据
content = tcp_client_socket.recv(1024).decode('gbk')  # 接收1024字节的数据，数据解码方式为gbk
print(f'服务器发送过来的数据:{content}')
# 5、关闭套接字对象
tcp_client_socket.close()
