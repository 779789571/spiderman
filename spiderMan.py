from common.utils import banner, checkEnv, handle_result
import fire
from plugin import baidu_spider,config
from common import handle_resultData,resultExport

class spiderMan(object):
    def __init__(self, keyword, format=None, pageNum=None, proxy=None, module=None):
        self.keyword = keyword
        self.format = format
        self.pageNum = pageNum
        self.proxy = proxy
        self.module = module
        self.runMod = []

    def search_Mod(self):
        duplicate_site = 0
        search_result = []
        if self.module == None:
            self.runMod = ['baidu_spider']
            baidu_result = baidu_spider.do(self.keyword)
            if baidu_result != -1:
                each_page_result = handle_result(baidu_result)  # 处理数据
                for i in range(len(each_page_result)):
                    for j in range(len(each_page_result[i])):
                        search_result.append(each_page_result[i][j])
                print('百度抓取{}页总共{}条数据'.format(config.page, len(search_result)))
            else:
                print('百度爬虫获取数据失败')

        if self.module == 'All':
            pass

        if self.module == 'bing':
            self.runMod == ['bing_spider']
            print('bing搜索暂未完成')
        #返回[(url,title)]格式的列表
        # print('重复域名共'+str(duplicate_site)+'个')
        return search_result

    # def result_export(self):
    #     if self.format == None:
    #         #设置默认格式为xlsx
    #         self.format = 'xlsx'
    #         print('default output format is {}'.format(self.format))
    #
    #     else:
    #         pass

    def main(self):
        banner()
        print('执行中...\n本次关键词：' + self.keyword)
        search_result = self.search_Mod()
        # 打印搜索模块结果列表
        # print(search_result)
        checked_result = handle_resultData.do(data=search_result,keyword=self.keyword)
        #打印已检查结果列表
        print(checked_result)
        resultExport.do(format=self.format,data=checked_result)
        # todo 写入excel


    # 程序入口
    def run(self):
        """
        信息收集
        USAGE: python3 spiderMan.py --keyword=abc run

        :param str keyword: search keyword 搜索关键词
        :param int Num: the number of result 导出url数量
        """
        checkEnv()
        self.main()

        print('运行结束🙆‍')


if __name__ == '__main__':
    fire.Fire(spiderMan)
    #关键词：刷赞网、刷钻网、代刷平台、24小时自助代刷平台、QQ 代刷网、低价QQ刷钻、免费QQ刷赞网\低价名片赞
    #spiderMan('intitle:刷赞网').run()

