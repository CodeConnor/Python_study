import socket

if __name__ == '__main__':
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server_socket.bind(('', 8080))
    tcp_server_socket.listen()

    while True:
        new_socket, ip_port = tcp_server_socket.accept()
        client_request_data = new_socket.recv(4096)
        if client_request_data:
            request_data = client_request_data.decode('utf-8')
            request_path = request_data.split(' ', maxsplit=2)[1]
            if request_path == '/':
                request_path = '/index.html'

            response_line = 'HTTP/1.1 200 OK\r\n'
            response_header = 'Server:PWB/2.0\r\n'
            response_body = ''.encode('utf-8')
            # 选择响应体内容
            try:
                with open('shopping' + request_path, 'rb') as f:
                    file_data = f.read()
                response_body = file_data
            except:
                response_line = 'HTTP/1.1 404 Not Found\r\n'
                response_header += 'Content-Type:text/html; charset=utf-8\r\n'
                response_body = '很抱歉，您所访问的页面不存在！'.encode('utf-8')
            finally:
                response_data = (response_line + response_header + '\r\n').encode('utf-8') + response_body
                new_socket.send(response_data)
                new_socket.close()