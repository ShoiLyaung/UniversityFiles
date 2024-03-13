import matplotlib.pyplot as plt

# 拥塞窗口大小和传输次数的示例数据
congestion_window = [i for i in range(1, 27)]
transmission_count = [1, 2, 4, 8, 16, 32, 33, 34, 35, 36,37,38,39,40,41,42,21,22,23,24,25,26,1,2,4,8]

# 创建折线图
plt.plot(congestion_window ,transmission_count , marker='.', linestyle='-')


# 显示网格
plt.grid(True)

# 设置坐标轴范围和刻度
plt.axis([1, 30, 0, 45])  # 设置X轴范围为0到11，Y轴范围为0到110

# 显示每个单位网格
plt.xticks(range(30))  # 设置X轴刻度显示每个单位
plt.yticks(range(0, 45, 4))  # 设置Y轴刻度显示每10个单位


plt.savefig('fig5-39.png')  # 保存为PNG文件，可以替换为其他格式如JPEG、PDF等
plt.show()
