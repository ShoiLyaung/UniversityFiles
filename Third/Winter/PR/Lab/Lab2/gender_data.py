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
    year = ''
    gender = ''
    # 从Excel文件夹读取数据
    for excel_file in os.listdir(folder_path):
        if excel_file.endswith('.xlsx') and excel_file.startswith('202'):
            excel_file_path = os.path.join(folder_path, excel_file)
            excel_data = pd.read_excel(excel_file_path)
            year = excel_file.split('.')[0][:4]
            excel_data['年份'] = year
            excel_dataframes.append(excel_data[['性别', '身高(cm)', '体重(kg)', '尺码', '年份']])
        elif excel_file=='boyandgirl2018.xlsx':
            excel_file_path = os.path.join(folder_path, excel_file)
            excel_data = pd.read_excel(excel_file_path)
            # excel_data = excel_data.dropna(subset=['性别'])
            excel_data = excel_data[excel_data['性别'].isin(['男', '女'])]
            excel_data['年份'] = '2018'
            excel_data = excel_data.rename(columns={'身高（cm）': '身高(cm)', '体重（kg）': '体重(kg)', '鞋码': '尺码'})
            excel_dataframes.append(excel_data[['性别', '身高(cm)', '体重(kg)', '尺码', '年份']])
    excel_data = pd.concat(excel_dataframes, ignore_index=True)
    
    # 从txt文件夹读取数据
    for txt_file in os.listdir(folder_path):
        if txt_file.endswith('.txt'):
            txt_file_path = os.path.join(folder_path, txt_file)
            year = txt_file.split('.')[0][-4:]
            if txt_file.startswith('boy'):
                gender = '男'
            if txt_file.startswith('girl'):
                gender = '女'
            txt_data = pd.read_csv(txt_file_path, sep='\s+', header=None, names=['身高(cm)', '体重(kg)', '尺码'], comment='#')
            txt_data['年份'] = year
            txt_data['性别'] = gender
            txt_dataframes.append(txt_data)
    txt_data = pd.concat(txt_dataframes, ignore_index=True)

    # 合并数据
    all_data = pd.concat([excel_data, txt_data], ignore_index=True)
    all_data['尺码'] = all_data['尺码'].round().astype(int)
    all_data['gender'] = 1 * (all_data['性别'] == '男')
    return all_data

def plot_histogram(data, color_by=None):
    """
    绘制数据中特定列的直方图。

    :param data: 包含数据的数据框。
    :param color_by: 用于区分特定类别的可选参数（例如，性别或年份）。

    Example usage:
    :plot_histogram(data)
    :plot_histogram(data, color_by='性别')
    :plot_histogram(data, color_by='年份')
    """
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    plt.figure(figsize=(14, 4))

    if color_by is None:
        color = ['blue', 'pink', 'red', 'orange', 'olive', 'cyan', 'green']
        for i, column in enumerate(['身高(cm)', '体重(kg)', '尺码'], start=1):
            plt.subplot(1, 3, i)
            plt.hist(data[column], 
                     bins=None if column == '尺码' else 20, 
                     color=color[i], 
                     edgecolor='black')
            plt.title(f'{column}分布')
            plt.xlabel(column)
            plt.ylabel('频数')
    else:
        categories = data[color_by].unique()
        color_mapping = {'男': 'blue', '女': 'pink', '2009': 'red', '2010': 'pink', '2011': 'orange', '2017': 'olive',
                         '2018': 'cyan', '2021': 'blue', '2022': 'green'}  # Add more colors as needed
        for i, column in enumerate(['身高(cm)', '体重(kg)', '尺码'], start=1):
            plt.subplot(1, 3, i)
            for category in categories:
                category_data = data[data[color_by] == category]
                plt.hist(category_data[column], 
                         bins=None if column == '尺码' else 20, 
                         color=color_mapping[category], 
                         edgecolor='black',
                         alpha=0.7, 
                         label=category)
            plt.title(f'{column}分布 - 区分{color_by}')
            plt.xlabel(column)
            plt.ylabel('频数')
            plt.legend()
    plt.tight_layout()
    plt.show()
