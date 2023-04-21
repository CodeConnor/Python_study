# TCP服务器端开发
import socket
# 1、创建服务器套接字对象
# tcp_server_socket内部只有服务器本身的信息，可以绑定端口、设置监听、接收客户端连接，但是本身不能收发数据
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2、绑定IP和端口
tcp_server_socket.bind(('127.0.0.1', 8000))
# 3、开始监听
tcp_server_socket.listen(128)  # 同时监听数量最多为128个，超出后连接请求会等待
# 4、接收客户端连接请求
# 每个客户端与服务器端连接时都会自动创建1个新套接字对象，这里将其保存在new_socket中
# 和tcp_server_socket不同。new_socket里保存了服务器端数据和客户端数据，所以服务器可以通过new_socket收发信息。
# ip_port: 客户端ip + 端口
new_socket, ip_port = tcp_server_socket.accept()
# 5、接收数据
content = new_socket.recv(1024).decode('gbk')
print(f'{ip_port}客户端发送过来的数据：{content}')
# 6、发送数据,响应数据给客户端（应答机制）
new_socket.send('信息已收到，over！'.encode('gbk'))
# 7、关闭套接字对象
new_socket.close()
tcp_server_socket.close()
