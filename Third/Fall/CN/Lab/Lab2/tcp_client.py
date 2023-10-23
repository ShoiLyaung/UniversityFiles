import socket

# 定义服务器地址和端口
serverHost = '127.0.0.1'  # 服务器IP地址
serverPort = 8080  # 服务器端口号

# 构建HTTP请求
request = f"GET /index.html HTTP/1.1\r\nHost: {serverHost}:{serverPort}\r\n\r\n"

# 创建客户端 socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverHost, serverPort))

# 发送请求给服务器
clientSocket.send(request.encode())

# 接收服务器的响应
response = clientSocket.recv(1024)

# 打印响应
print(response.decode())

# 关闭客户端 socket
clientSocket.close()
