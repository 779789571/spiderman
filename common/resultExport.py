import csv
from plugin.config import output_format, path
from common.utils import checkFilename, checkPath, checkFormat


class ResultExport(object):
    """
    export the result，此类用来导出结果
    :param format output format格式
    :param filrname output file's name导出文件名
    :param path output path 导出路径
    :param data the result 结果列表
    """

    def __init__(self, data, format=None, filename=None, path=None):
        self.format = format
        self.filename = filename
        self.path = path
        self.data = data

    def export_data(self, data, format, path):
        print('去重、筛选完毕，开始导出数据..')
        if format == 'csv':
            headers = ['序号', 'site', 'title', '发现时间', '关键词']
            with open(path, 'w', encoding='utf-8') as f:

                writer = csv.DictWriter(f, headers)
                writer.writeheader()
                for row in data:
                    writer.writerow(row)
            print('导出完毕')

    def run(self):
        filename = checkFilename(self.filename)
        format = checkFormat(self.format)
        path = checkPath(path=self.path, name=filename, format=format)
        print(filename, path)
        self.export_data(data=self.data, format=format, path=path)


def do(format, data):
    output = ResultExport(format=format,data=data,)
    output.run()


if __name__ == '__main__':
    format = 'csv'
    data = [{'序号': '1', 'site': 'wst520.top', 'title': '想保持热情的小猫鼠 – 断剑重铸之日,其势归来之时。', '发现时间': '20200526', '关键词': '嘿嘿'}]
    output = ResultExport(data=data)
    output.run()
