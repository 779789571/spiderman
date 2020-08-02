from bs4 import BeautifulSoup
import time
import requests

url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=monline_4_dg&wd=%E7%99%BE%E5%BA%A6%E7%88%AC%E8%99%AB%20%E8%8E%B7%E5%8F%96title&oq=%25E7%2599%25BE%25E5%25BA%25A6%25E7%2588%25AC%25E8%2599%25AB%2520beautiful&rsv_pq=9007e82b000b8ea8&rsv_t=f316tyaVw01yuVCk84KnrcgLUkovVrwQlvE62mhi%2FKyUkNnUqc9BCvj6jhpSyBHnoMo7&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=29&rsv_sug1=18&rsv_sug7=100&rsv_sug2=0&rsv_btype=t&inputT=5955&rsv_sug4=6269&rsv_sug=1'
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

resp = requests.get(url=url, headers=baidu_header)
print((resp.content))
# print(resp.text)
soup = BeautifulSoup(resp.content, 'lxml')
tagh3 = soup.find_all('h3')
for h3 in tagh3:
    href = h3.find('a').get('href')
    title = h3.find('a').strings
    # print('testTitle' + title)
    # print('href' + href)
    baidu_url = requests.get(url=href, headers=baidu_header, allow_redirects=False)
    real_url = baidu_url.headers['Location']  # 得到网页原始地址
    #realUrl,baiduhref
    # print(real_url,href)
    title_list = []
    for string in title:
        # print(string)
        comb = ''.join(string)
        title_list.append(comb)

    print(''.join(title_list))