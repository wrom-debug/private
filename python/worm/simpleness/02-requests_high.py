import requests
from requests.packages import urllib3
import urllib.error
import socket
# 上传文件
"""
files={"文件名称":open("路径","打开方式",encoding="编码格式")}
r=requests.post("url",files=files)
"""
# 获取cookies

"""
r=requests.get("http://www.baidu.com")
print(r.cookies.items)
for key,value in r.cookies.items():
    print(key+"="+value)
"""
# 获取的cookies要通过遍历读取
# 使用cookies登录
"""headers={"Cookie":'BIDUPSID=DEFE4AC66F6EDFB47200306AC950D04E; PSTM=1584286908; BAIDUID=DEFE4AC66F6EDFB4B8E7767A505076E6:FG=1; H_PS_PSSID=30972_1426_31122_21118_30823_22157; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; PSINO=5; BDUSS=J1dWt2T2RFblJjUVM3bkt-SEI3cm91NG9MTn40Qlg3aHBSTVp0ZDBDcm0tcUplSVFBQUFBJCQAAAAAAAAAAAEAAABx06IwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOZte17mbXteaj; cflag=13%3A3',
'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
r=requests.get("https://pan.baidu.com/disk/home?#/all?path=%2F&vmode=list",headers=headers)
r.encoding=r.apparent_encoding
print(r.text)"""
# 没有测试成功
# 会话维持
"""requests.get("http://httpbin.org/cookies/set/number/634514726")
r=requests.get("http://httpbin.org/cookies")
r.encoding=r.apparent_encoding
print(r.text)

s=requests.Session()
s.get("http://httpbin.org/cookies/set/number/634514726")
r=s.get("http://httpbin.org/cookies")
print(r.text)"""
# Session对象的与requests类似，不过可以每次请求类似新开一个浏览器选项卡，来达到多个请求维持在一个会话中
# http升级成https需要服务器有ssl或者tls来对http数据来进行加密
#https请求
"""urllib3.disable_warnings()
r=requests.get("https://www.12306.cn",verify=False)
print(r)"""
# 12306已经升级到正确的ssl证书了，对于没有正确的ssl网站可以在请求中verify参数设定为False
# 但是设置verify会导致程序出警告 可以使用requests.packages.urllib3的urllib3.disable_warings()来忽略警告
# 设置代理
"""proxies={"http":"http://123.207.217.179:1080",}
headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
r=requests.get("http://httpbin.org/get",proxies=proxies)
print(r.text)"""
# 使用socks需要导入pip install 'requests[socks]'
# 在proxies={“http”：“socks5：//uesr:password@host:port}
# 超时
# 在请求中设置参数timeout
"""r=requests.get("http://www.baidu.com",timeout=1)"""
# 超时断言异常使用try模板也接不了
# 网页认证
"""r=requests.get("url",auth=("username","password"))"""
# 设置auth参数（还没试过）
# 构造数据结构再请求
url="http://httpbin.org/post"
data={"name":"age"}
headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
s=requests.Session()
req=requests.Request("POST",url,data=data,headers=headers,)
prepped=s.prepare_request(req)
r=s.send(prepped)
print(r.text)
# 构造的使用Request构造请求在使用Session对象用send方法发送