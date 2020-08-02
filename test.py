import requests

url = 'https://www.bing.com/search?q=bbb&sp=-1&pq=1&sc=8-1&qs=n&sk=&cvid=C5AC91C7135B4FB7AC4918958BF7E362&first=1&FORM=PERE'
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
resp = requests.get(url)
print(resp.content)