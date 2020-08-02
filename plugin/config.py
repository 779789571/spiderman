# Default setting
# 包含的爬虫
import pathlib
include = ['baidu', 'bing','fofa']
exclude = ['google']

#准备写多个匹配规则，通过修改rule来调整获取的数据
rule = 1

# 代理模式 未完成
proxy_config = {}

#百度 header头
baidu_header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection': 'keep-alive',
    'Cookie': 'BAIDUID=881A408844E5FCBDB218F7B9ED62D294:FG=1; BIDUPSID=881A408844E5FCBDB218F7B9ED62D294; PSTM=1568633058; BDUSS=M5eXhWb2xIaW9TTXpPaHlHYnB3SjJHOXhXaU9Pfm14NnJ-Tjl6WGVFRlN1MzVlSVFBQUFBJCQAAAAAAAAAAAEAAADAriBGc2QzNWYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFIuV15SLldeWl; H_PS_PSSID=1426_31326_21099_31111_31463_30823; BD_UPN=133252; sug=3; sugstore=0; ORIGIN=0; bdime=0; H_PS_645EC=65944KQFbJMJdcFml1gtPtOgCfo9kB%2FIiYtHVe6SoPp0hVAw01RaaIphEqQ%2Bxv0ra%2FVu; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; COOKIE_SESSION=0_0_1_1_0_4_1_0_1_1_14_2_0_0_0_0_0_0_1572416215%7C1%230_0_1589857301%7C1%7C1; delPer=0; BD_CK_SAM=1; PSINO=5; BDSVRTM=82',
    'Host': 'www.baidu.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:76.0) Gecko/20100101 Firefox/76.0',
}
bing_header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'text/xml',
    'Content-Length': '8343',
    'Origin': 'https://www.bing.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.bing.com/?toWww=1&redig=A00835B216F54F998A8E1E25901B1C87',
    'Cookie':'MUID=0F37618D450962673B126F2D447663B4; _EDGE_S=SID=09389419D2BF6E0834699B1FD3C06F11; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=51494707957D47A4AE3959E288C55863&dmnchg=1; SRCHUSR=DOB=20200713; _SS=SID=09389419D2BF6E0834699B1FD3C06F11&R=0&RB=0&GB=0&RG=0&RP=0; _HPVN=CS=eyJQbiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyMC0wNy0xM1QwMDowMDowMFoiLCJJb3RkIjowLCJEZnQiOm51bGwsIk12cyI6MCwiRmx0IjowLCJJbXAiOjJ9; MUIDB=0F37618D450962673B126F2D447663B4; SRCHHPGUSR=WTS=63730205160&HV=1594608362; ipv6=hit=1594611961657&t=4; _RwBf=mtu=0&g=0&o=2&p=&c=&t=0&s=0001-01-01T00:00:00.0000000+00:00&ts=2020-07-13T02:46:01.6498412+00:00&ssg=0',
    'TE': 'Trailers'
}
#爬虫线程
thread_num = 10

# 输出格式 默认导出csv格式，暂时只csv，txt 后续添加json,xlsx,html
output_format = 'csv'
output_num = 'all'#导出数据数,默认全部导出
path = pathlib.Path(__file__).parent.parent #结果导出路径，默认在spiderMan.py的同目录下
result_save_dir = path.joinpath('result')  # 结果保存目录
page = 10 #爬取网站页数
delay = 0.5 #设置爬取延迟