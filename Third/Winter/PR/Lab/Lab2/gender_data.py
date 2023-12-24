import pandas as pd
import os
import matplotlib.pyplot as plt

def read_data_from(folder_path = 'genderdata'):
    """
    从文件夹中读取数据
    :param folder_path: 文件夹路径
    :return: 读取的数据
    """
    excel_dataframes = []
    txt_dataframes = []

    # 从Excel文件夹读取数据
    for excel_file in os.listdir(folder_path):
        if excel_file.endswith('.xlsx') and excel_file.startswith('202'):
            excel_file_path = os.path.join(folder_path, excel_file)
            excel_data = pd.read_excel(excel_file_path)
            excel_dataframes.append(excel_data[['性别', '身高(cm)', '体重(kg)', '尺码']])
        elif excel_file=='boyandgirl2018.xlsx':
            excel_file_path = os.path.join(folder_path, excel_file)
            excel_data = pd.read_excel(excel_file_path)
            # excel_data = excel_data.dropna(subset=['性别'])
            excel_data = excel_data[excel_data['性别'].isin(['男', '女'])]
            excel_data = excel_data.rename(columns={'身高（cm）': '身高(cm)', '体重（kg）': '体重(kg)', '鞋码': '尺码'})
            excel_dataframes.append(excel_data[['性别', '身高(cm)', '体重(kg)', '尺码']])
    excel_data = pd.concat(excel_dataframes, ignore_index=True)
    
    # 从txt文件夹读取数据
    for txt_file in os.listdir(folder_path):
        gender = '男'
        if txt_file.endswith('.txt'):
            txt_file_path = os.path.join(folder_path, txt_file)
            if txt_file.startswith('boy'):
                gender = '男'
            if txt_file.startswith('girl'):
                gender = '女'
            txt_data = pd.read_csv(txt_file_path, sep='\s+', header=None, names=['身高(cm)', '体重(kg)', '尺码'], comment='#')
            txt_data['性别'] = gender
            txt_dataframes.append(txt_data)
    txt_data = pd.concat(txt_dataframes, ignore_index=True)

    # 合并数据
    all_data = pd.concat([excel_data, txt_data], ignore_index=True)
    all_data['尺码'] = all_data['尺码'].round().astype(int)
    return all_data

def visualize_data(data):
    """
    可视化数据
    :param data: 数据
    """
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    # 可视化每个维度的直方图
    plt.figure(figsize=(15, 10))
    # 绘制身高的直方图
    plt.subplot(2, 2, 1)
    plt.hist(data['身高(cm)'], bins=20, color='blue', edgecolor='black')
    plt.title('身高分布')
    plt.xlabel('身高')
    plt.ylabel('频数')
    # 绘制体重的直方图
    plt.subplot(2, 2, 2)
    plt.hist(data['体重(kg)'], bins=20, color='green', edgecolor='black')
    plt.title('体重分布')
    plt.xlabel('体重')
    plt.ylabel('频数')
    # 绘制尺码的直方图
    plt.subplot(2, 2, 3)
    plt.hist(data['尺码'], color='orange', edgecolor='black')
    plt.title('尺码分布')
    plt.xlabel('尺码')
    plt.ylabel('频数')
    plt.tight_layout()
    plt.show()

    # 可视化每个维度的直方图，区分男女性别
    plt.figure(figsize=(15, 10))
    # 绘制身高的直方图
    plt.subplot(2, 2, 1)
    for gender, color in [('男', 'blue'), ('女', 'pink')]:
        gender_data = data[data['性别'] == gender]
        plt.hist(gender_data['身高(cm)'], bins=20, color=color, edgecolor='black', alpha=0.7, label=gender)
    plt.title('身高分布')
    plt.xlabel('身高')
    plt.ylabel('频数')
    plt.legend()
    # 绘制体重的直方图
    plt.subplot(2, 2, 2)
    for gender, color in [('男', 'blue'), ('女', 'pink')]:
        gender_data = data[data['性别'] == gender]
        plt.hist(gender_data['体重(kg)'], bins=20, color=color, edgecolor='black', alpha=0.7, label=gender)
    plt.title('体重分布')
    plt.xlabel('体重')
    plt.ylabel('频数')
    plt.legend()
    # 绘制尺码的直方图
    plt.subplot(2, 2, 3)
    for gender, color in [('男', 'blue'), ('女', 'pink')]:
        gender_data = data[data['性别'] == gender]
        plt.hist(gender_data['尺码'], color=color, edgecolor='black', alpha=0.7, label=gender)
    plt.title('尺码分布')
    plt.xlabel('尺码')
    plt.ylabel('频数')
    plt.legend()
    plt.tight_layout()
    plt.show()

    # 可视化数据
    plt.figure(figsize=(10, 6))
    # 绘制所有数据
    for gender, color, marker in [('男', 'blue', 'x'), ('女', 'red', 's')]:
        gender_data = data[data['性别'] == gender]
        plt.scatter(gender_data['身高(cm)'], gender_data['体重(kg)'], label=f'所有数据 ({gender})', color=color, marker=marker)
    plt.xlabel('身高')
    plt.ylabel('体重')
    plt.title('身高体重分布')
    plt.legend()
    plt.show()
