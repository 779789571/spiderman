import plugin.config
import time
import requests
from pathlib import Path
def banner():
    print('*'*30)
    print('         *安恒信息*\n  design by jinx0v0')
    print('*'*30)

def checkEnv():
    pass
    print('checking python Env')

#处理各个search模块的数据
def handle_result(result):
    each_page_result_list = []
    for i in range(len(result)):
        each_page_result = list(result[i])
        #打印每一页搜索结果
        # print(each_page_result)
        each_page_result_list.append(each_page_result)
    #打印百度搜索所有结果
    # print(each_page_result_list)
    #二维数组转换为一维
    return each_page_result_list

def checkFilename(filename):#检查文件名是否合法
    if filename == None:
        string = str(time.time()).replace('.','')
        return string
    else:
        filename = repr(filename).replace('\\','/')
        filename  = filename.replace('/','')
        filename = filename.replace('\'', '')
        print(filename)
        return filename

def checkFormat(format):
    formatList = ['txt','csv']#todo 后续添加xlsx，html
    if format == None:
        format = 'csv'
        return format
    elif format in formatList:
        return format
    else:
        print('输出格式参数有问题，请检查。改为输出csv')
        format = 'csv'
        return format
def checkPath(path,name,format):
    filename = f'{name}.{format}'
    default_path = plugin.config.result_save_dir.joinpath(filename)
    if isinstance(path, str):
        path = repr(path).replace('\\', '/')  # 将路径中的反斜杠替换为正斜杠
        path = path.replace('\\', '')  # 去除/的字符，转义
    else:
        path = default_path
    path = Path(path)
    if not path.suffix:  # 输入是目录的情况
        path = path.joinpath(filename)
    parent_dir = path.parent
    if not parent_dir.exists():
        # logger.log('ALERT', f'{parent_dir} does not exist, directory will be created')
        parent_dir.mkdir(parents=True, exist_ok=True)
    if path.exists():
        # logger.log('ALERT', f'The {path} exists and will be overwritten')
        print('the {} exists and wiil be ocerwritten'.format(path))
    return path

