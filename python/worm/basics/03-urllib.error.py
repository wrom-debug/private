import urllib.error
import urllib.request
# try:
#     response=urllib.request.urlopen("http://www.xiaoshuowu.com/robots.txt")
# except urllib.error.URLError as e:
#     print(e)
try:
    response = urllib.request.urlopen("http://www.xiaoshuowu.com/robots.txt")
except urllib.error.HTTPError as e:
    print(e.reason,e.code,e.headers,sep="\n")
# HTTPError是URLError的子类来处理http请求出现的错误
# reason属性是返回错误原因    code属性是返回请求状态码  headers属性返回请求头的信息
except urllib.error.URLError as e:
    print(e.reason, e.code, e.headers, sep="\n")
else:
    print("request success")

# 使用异常处理模板优先判断是否为http错误，再判断url错误，如果没有错误就输出请求成功
# 有时reason返回的也可能不是字符串而是对象
