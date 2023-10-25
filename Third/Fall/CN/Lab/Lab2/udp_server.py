from socket import *
import random
# 创建一个 UDP 套接字 ( SOCK_DGRAM )
serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',12000))
while True:
    rand = random.randint(0,10)
    message, address = serverSocket.recvfrom(1024)
    print(message)
    message = message.upper()
    # 模拟 30% 的数据包丢失。
    if rand < 4:
        continue
    serverSocket.sendto(message, address)
