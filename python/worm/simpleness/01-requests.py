import requests

a=requests.request("get","http://httpbin.org/get")
# 这种凡是也可以请求，输入模式用法和其他请求一样
data={
    "name":"a",
    "age":"18"
}
hard={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
r=requests.get("http://httpbin.org/get",params=data,headers=hard)
# 可以在请求中添加headers头信息（user-agent什么系统什么浏览器访问的），添加params来重构url
# print(r.text)
# 一般在使用text属性前会修改r.encoding=r.apparent_encoding来重新定义编码格式
# 可以输出请求到的str内容
# print(r.json())
# 可以输出请求的json数据
# print(r.content)
# 可以输出请求到的二进制内容
# 请求实例还有一下属性status_code响应状态码（也可以直接查看ok属性是否为Ture）   headers响应头 url跳转后的url
# encoding响应的推测编码   apparent_encoding更近准的编码格式 修改的text的显示编码
r=requests.post("http://httpbin.org/post",data=data)
print(r.encoding)
print(r.apparent_encoding)
print(r.text)
# 发送的数据就在form中
