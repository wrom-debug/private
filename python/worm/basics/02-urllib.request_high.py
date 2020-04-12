import urllib.request
import urllib.error
import http.cookiejar


def verify():
    # 验证——用于对付弹出身份验证
    """实例化密码管理对象，并通过add_password方法添加对应的账户密码与url，再继承到认证管理类的handler，
    在用buli_opener将handler转换成opener，最后使用open方法请求
    """
    uername="username"
    password="pasword"
    url="http://localhost:5000/"
    p=urllib.request.HTTPPasswordMgrWithDefaultRealm()
    p.add_password(None,url,uername,password)
    auth_handler=urllib.request.HTTPBasicAuthHandler(p)
    opener=urllib.request.build_opener(auth_handler)
    try:
        result=opener.open(url)
        html=result.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e :
        print(e.reason)

def agency():
    #代理
    """
    定义代理实例并通过build_opener转换再使用open请求
    """
    proxy=urllib.request.ProxyHandler({"http":"123.207.217.179:1080"})
    opener=urllib.request.build_opener(proxy)
    try:
        reponse=opener.open("http://httpbin.org/get")
        html=reponse.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e :
        print(e.reason)
def get_cookies():
    # 获取cookies
    """
    生成cookies罐集成给cookie处理类，再转换成openre，最后使用open方法请求，可以使最开始的cookies罐实例有cookies
    """
    cookie=http.cookiejar.CookieJar()
    handler=urllib.request.HTTPCookieProcessor(cookie)
    opener=urllib.request.build_opener(handler)
    response=opener.open("http://ww.baidu.com")
    print(cookie)

def save_cookies():
    #获取浏览器格式cookies并保存到c.txt文件中
    """
    与获取先同结构只是修改cookies罐类型为浏览器cookie罐并调用save方法保存，其中ignore忽略丢弃与到期
    cookies文件还有别的形式lwp
    """
    fil="cookies.txt"
    cookie=http.cookiejar.MozillaCookieJar(fil)
    handler=urllib.request.HTTPCookieProcessor(cookie)
    opener=urllib.request.build_opener(handler)
    response=opener.open("http://ww.baidu.com")
    cookie.save(ignore_discard=True,ignore_expires=True)


def main():
    agency()

if __name__ == '__main__':
    main()