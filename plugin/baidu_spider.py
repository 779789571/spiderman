from bs4 import BeautifulSoup
import time
import requests
import re
from urllib import parse
from multiprocessing.dummy import Pool
from plugin.config import baidu_header, thread_num, rule, page, delay


# 这部分爬虫参考了oneforall，向开源作者表示感谢。https://github.com/shmilylty/OneForAll

class Baidu_spider(object):

    def __init__(self, keywords):
        self.keywords = keywords
        self.addr = 'https://www.baidu.com/s'
        # self.limit_num = 750  # 限制搜索条数
        self.header = baidu_header
        self.thread_num = thread_num
        self.rule = 1
        self.page_MAXNum = page
        self.delay = delay

    def get_resp(self,url):

        rep = requests.get(url,headers = baidu_header)
        if rep.status_code == 200:
            return rep.content
        else:return -1
    # 获取页面
    def get_data(self, keyword):
        # 单线程
        """

        :param keyword:
        :return:

        time.sleep(self.delay)
        resp_content = []
        # url编码
        # keyword = parse.quote(keyword)

        # 打印关键字
        # print(keyword)

        for page in range(self.page_MAXNum):
            params = {'wd': keyword,
                      'pn': page * 10,
                      'ie': 'utf-8'
                      }

            resp = requests.get(self.addr, params=params, headers=baidu_header)
            if resp.status_code == 200:
                resp_content.append(resp.content)
        """


        #多线程
        resp_content = []
        url_list = []
        for page in range(self.page_MAXNum):
            params = self.addr+'?wd='+keyword+'&pn='+str(page*10)+'&ie=utf-8'
            url_list.append(params)
        #打印访问的url
        # print(url_list)
        #线程池
        pool = Pool(processes=self.thread_num)

        resp_content = pool.map(self.get_resp,url_list)
        # print(resp_content)


        return resp_content


    # 处理返回包html,返回真实的url及title列表
    def handle_data(self, resp):
        real_url_list = []
        title_list = []
        self.resp = resp
        if self.rule == 1:
            # todo 处理数据
            soup = BeautifulSoup(self.resp, 'lxml')
            tagh3 = soup.find_all('h3')
            for h3 in tagh3:
                href = h3.find('a').get('href')
                # 打印baidu搜索获取的链接
                # print(href)

                title = h3.find('a').strings  # 需要拼接
                try:
                    baidu_url = requests.get(url=href, headers=self.header, allow_redirects=False)
                except:
                    str = '访问不了' + href
                    # print(str)
                    real_url_list.append(str)
                real_url = baidu_url.headers['Location']  # 得到网页原始地址

                # 打印真实url
                # print(real_url)

                # all.write(real_url + '\n')
                real_url_list.append(real_url)
                # 拼接title
                _title = []
                for string in title:
                    # print(string)
                    comb = ''.join(string)
                    _title.append(comb)
                # 打印标题title
                # print(''.join(_title))
                title_list.append(''.join(_title))

            return real_url_list, title_list

    # 爬虫执行入口
    def run(self):
        result_list = []
        keyword = self.keywords
        print('baiduSpider Mod on 😁')

        # for i in range(self.page):
        #     data = self.get_data(self.keywords)
        #     result = self.handle_data(data)
        resp_text = self.get_data(keyword)
        for i in range(len(resp_text)):
            baidu_url_list, title_list = self.handle_data(resp_text[i])
            result_list.append(zip(baidu_url_list, title_list))
            # print(baidu_url_list,title_list)

        # 打印爬虫数据
        # for _ in range(len(result_list)):
        #     print(list(result_list[_]))

        if result_list:
            return result_list
        else:
            return -1


def do(keywords):
    spider = Baidu_spider(keywords=keywords)
    result = spider.run()
    return result


if __name__ == '__main__':
    sp = Baidu_spider(keywords='bbb')
    print(sp.run())
