import datetime
import os
import pandas as pd
from openpyxl import load_workbook
from urllib.parse import urlparse


class Handle_resultData(object):
    """
    此类用来处理url搜索结果，去重
    输出结果为字典 {'序号':'1','site':'wst520.top','title':'想保持热情的小猫鼠 – 断剑重铸之日,其势归来之时。','发现时间':'20200526','关键词':'嘿嘿'}
    """

    def __init__(self, data, keyword):
        self.data = data
        self.keyword = keyword

    # 检查新域名是否已在列表中
    def check_if_existed(self, url, existed_domain_list):
        if url.startswith('http'):
            domain = urlparse(url).netloc.replace('www.', '')#todo 去重可能有问题
        else:
            domain = url
        if domain not in existed_domain_list:
            return -1
        else:
            return 1



    # 加载已存在的域名，返回列表
    def load_exist_domain(self):
        try:
            print('开始去重、比对已存在域名..')
            existed_domain_list = []  # 已存在域名汇总列表
            file_path = (os.path.abspath(os.path.dirname(__file__)).split('spiderMan')[
                             0] + 'spiderMan/result/result_all.xlsx')
            # print(file_path)
            given_list_sheet = []

            # excel表1
            df = pd.read_excel(file_path, sheet_name='平台类')
            for i in df.index.values:
                row_data = dict(df.loc[i, ['平台域名/IP/软件MD5值']])
                for key in row_data:
                    # given_list.append(row_data[key])
                    if row_data[key].startswith('http'):
                        _domain = urlparse(row_data[key]).netloc.replace('www.', '')
                        existed_domain_list.append(_domain)
                    else:
                        existed_domain_list.append(row_data[key].replace('www.', ''))
            # excel表2

            df2 = pd.read_excel(file_path, sheet_name='黑产信息交流群组')
            for i in df2.index.values:
                row_data = dict(df2.loc[i, ['类型（域名/QQ群号/telegram群号）', '域名/QQ群号/telegram群号']])
                given_list_sheet.append(row_data)
            # print(given_list)
            # print(given_list_sheet[0]['类型（域名/QQ群号/telegram群号）'])
            for i in range(len(given_list_sheet)):
                if given_list_sheet[i]['类型（域名/QQ群号/telegram群号）'] == '域名':
                    # 打印表2的域名
                    # print(given_list_sheet[i]['域名/QQ群号/telegram群号'])
                    if given_list_sheet[i]['域名/QQ群号/telegram群号'].startswith('http'):
                        _domain = urlparse(given_list_sheet[i]['域名/QQ群号/telegram群号']).netloc.replace('www.', '')
                        existed_domain_list.append(_domain)
                    else:
                        existed_domain_list.append(given_list_sheet[i]['域名/QQ群号/telegram群号'])

        except Exception as e:
            print(e)

        return existed_domain_list

    def run(self):
        result = []
        existed_domain_list = []
        # 统计新增个数
        number = 0
        today = datetime.date.today()
        # 获取已存在域名
        if os.path.exists(os.path.abspath(os.path.dirname(__file__)).split('spiderMan')[
                              0] + 'spiderMan/result/domain_all.txt'):
            print('存在spiderMan/result/domain_all.txt，将使用此文件导入已存在的域名')
            with open(os.path.abspath(os.path.dirname(__file__)).split('spiderMan')[
                          0] + 'spiderMan/result/domain_all.txt', 'r') as f:
                lines = f.readlines()
                for line in lines:
                    # print(line)
                    existed_domain_list.append(line.strip('\n'))


        else:
            existed_domain_list = self.load_exist_domain()
        # print(existed_domain_list)
        for i in range(len(self.data)):
            if self.check_if_existed(self.data[i][0], existed_domain_list) == -1:
                number += 1
                dict = {'序号': number, 'site': self.data[i][0], 'title': self.data[i][1], '发现时间': str(today),'关键词':self.keyword}
                existed_domain_list.append(urlparse(self.data[i][0]).netloc.replace('www.', ''))
                result.append(dict)
            elif self.check_if_existed(self.data[i][0], existed_domain_list) == 1:
                print('重复域名：'+self.data[i][0])
        file_save_path = (os.path.abspath(os.path.dirname(__file__)).split('spiderMan')[
                              0] + 'spiderMan/result/domain_all.txt')
        # print(existed_domain_list)
        with open(file_save_path, 'w') as f:
            for i in range(len(existed_domain_list)):
                if existed_domain_list[i] == '':
                    continue
                f.writelines(existed_domain_list[i] + '\n')
        # 打印返回结果列表
        # print(result)

        return result
def do(data, keyword):
    final_result = Handle_resultData(data=data, keyword=keyword)
    result = final_result.run()
    return result


if __name__ == '__main__':
    data = [('https://wst520.top/%3Fp%3D196', '重装wordpress的坑 – 想保持热情的小猫鼠'),
            ('https://wst520.top/', '想保持热情的小猫鼠 – 断剑重铸之日,其势归来之时。'),
            ('https://wst520.top/%3Fpaged%3D2', '想保持热情的小猫鼠 –第2页 – 断剑重铸之日,其势归来之时。'),
            ('https://wst520.top/%3Fp%3D196', '重装wordpress的坑 – 想保持热情的小猫鼠'),
            ('https://wst520.top/', '想保持热情的小猫鼠 – 断剑重铸之日,其势归来之时。'),
            ('https://wst520.top/%3Fpaged%3D2', '想保持热情的小猫鼠 –第2页 – 断剑重铸之日,其势归来之时。'),
            ('https://wst520.top/%3Fp%3D196', '重装wordpress的坑 – 想保持热情的小猫鼠'),
            ('https://wst520.top/', '想保持热情的小猫鼠 – 断剑重铸之日,其势归来之时。'),
            ('https://wst520.top/%3Fpaged%3D2', '想保持热情的小猫鼠 –第2页 – 断剑重铸之日,其势归来之时。'),
            ('https://wst520.top/%3Fp%3D196', '重装wordpress的坑 – 想保持热情的小猫鼠'),
            ('https://wst521.top/', '想保持热情的小猫鼠 – 断剑重铸之日,其势归来之时。'),
            ('https://mgmxc77.com/%3Fpaged%3D2', '想保持热情的小猫鼠 –第2页 – 断剑重铸之日,其势归来之时。')]
    keyword = 'site:wst520.top'
    do(data=data, keyword=keyword)
