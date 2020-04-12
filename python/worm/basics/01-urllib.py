import urllib.request
import urllib.error
import urllib.robotparser
import urllib.parse
import socket


# urllib有4个模块   request是请求HTTP的     error是进行异常处理    parse处理url      robotparser是处理爬虫是否可爬的
response=urllib.request.urlopen("http://www.baidu.com")
# get方式请求返回HTTPResposne类型对象
# respons有read（）读取  getheader(name)获取响应头中的name属性值   status响应状态码
print(response.read())
#请求并打印出爬取到的内容
data=bytes("a=b",encoding="utf-8")
# response=urllib.request.urlopen("http://httpbin.org/post",data=data)
# post方式请求  传递的数据要是字节流  还需制定编码格 除了data还有context传递ssl设置      cafile和capath设定ca证书和路经用于https
# print(response.read().decode("utf-8"))
try:
    response=urllib.request.urlopen("http://www.baidu.com",timeout=0.01)
except urllib.error.URLError as e:
    print(e)
    # if isinstance(e.reason,socket.timeout):

    print("timeout")
# 设置请求超时时间，超时后会报错，并判断错误类型是是否是超时类型
"""url="http://httpbin.org/post"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}
req=urllib.request.Request(url,headers=headers,data=data,method="POST")
response=urllib.request.urlopen(req)
print(response.read().decode("utf-8"))"""
# 使用Request类将请求的uel（网站），headers（请求头），data（post传输的数据），method请求方式组合成一个类   headers还可以调用实例的.add_headers来添加



