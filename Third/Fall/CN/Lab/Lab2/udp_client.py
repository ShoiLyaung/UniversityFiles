from socket import *
import time

# 创建套接字
clientSocket = socket(AF_INET, SOCK_DGRAM)
# 设置套接字超时为 1 秒
clientSocket.settimeout(1)
# 目标服务器的地址和端口
serverAddress = ('localhost', 12000)
# serverAddress = ('shoilyaung.space', 12000)
# 发送和接收的报文数量
sentPings = 0
receivedPings = 0
# 存储所有 RTT 的列表
rtts = []

# 发送 1000 个 ping 报文
for i in range(1000):
    startTime = time.time()

    # 发送 ping 报文，包含一个时间戳
    message = f'Ping {i+1} {startTime}'
    clientSocket.sendto(message.encode(), serverAddress)
    sentPings += 1

    try:
        # 接收服务器的响应
        response, _ = clientSocket.recvfrom(1024)
        endTime = time.time()

        # 计算并打印 RTT
        rtt = endTime - startTime
        rtts.append(rtt)
        print(f'Received: {response.decode()}, RTT: {rtt:.6f} sec')
        receivedPings += 1
    except timeout:
        # 如果在超时期限内没有收到响应，打印消息丢失
        print('Request timed out')

# 计算丢包率并打印结果
lossRate = (sentPings - receivedPings) / sentPings * 100
print(f'Packet loss rate: {lossRate:.2f}%')
# 计算并打印最小、最大和平均 RTT
if rtts:
    minRtt = min(rtts)
    maxRtt = max(rtts)
    avgRtt = sum(rtts) / len(rtts)
    print(f'Min RTT: {minRtt:.6f} sec, Max RTT: {maxRtt:.6f} sec, Avg RTT: {avgRtt:.6f} sec')

# 关闭套接字
clientSocket.close()
