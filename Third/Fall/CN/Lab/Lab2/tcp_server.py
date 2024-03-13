# 导入需要的模块
import socket
import threading
import os

# 定义服务器监听地址和端口
serverHost = '127.0.0.1'  # 服务器IP地址
serverPort = 8080  # 服务器端口号

# 准备服务器端 socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((serverHost, serverPort))
serverSocket.listen(1)
print(f"Server is listening on {serverHost}:{serverPort}")

def handle_client(clientSocket):
    # 接收客户端的HTTP请求
    request = clientSocket.recv(1024).decode()
    
    # 解析HTTP请求，提取请求文件名
    filename = request.split()[1]
    filename = filename[1:]  # 去除开头的"/"
    
    # 构建响应报文
    try:
        with open(filename, 'rb') as file:
            content = file.read()
            response = f"HTTP/1.1 200 OK\r\nContent-Length: {len(content)}\r\n\r\n".encode() + content
    except FileNotFoundError:
        response = b"HTTP/1.1 404 Not Found\r\n\r\nFile Not Found"
    
    # 发送响应给客户端
    clientSocket.send(response)
    
    # 关闭客户端连接
    clientSocket.close()

while True:
    # 建立连接
    print('Ready to serve...')
    clientSocket, addr = serverSocket.accept()
    
    # 创建新线程来处理客户端请求
    client_thread = threading.Thread(target=handle_client, args=(clientSocket,))
    client_thread.start()
