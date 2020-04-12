# 爬虫是否可爬，网站协议类型
# 
import urllib.robotparser
import requests
def RobotsGetIsOk(Feed,Worm,):
    """判断目标网站是否有爬虫协议，目标资源是否可爬是否"""
    if(len(Feed)!=0 and len(Worm)!=0) :
        # 对输入进行判断
        mod=getmode(Feed)
        if  not Feed.startswith("http"):
            Feed=mod+Feed
        FeedManual=Feed+'/robots.txt'
        FeedManualExistence=RobotsExistence(FeedManual)
        if FeedManualExistence != 404 :
            print("协议存在，饲料机运行")
            FeedMachine=urllib.robotparser.RobotFileParser()
            # 组装饲料机
            FeedMachine.set_url(FeedManual)
            # 投入饲料手册
            FeedMachine.read()
            # 开启饲料机
            return FeedMachine.can_fetch(Worm,Feed)
        else:
            print("饲料无害，尽情食用")
            return

def RobotsExistence(FeedManual):
    # 对饲料手册是否存在进行判断
    re=requests.get(FeedManual)
    return re.status_code

def get_html(url):
    # get请求       输入url     返回网页的html源码
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
    a=requests.get(url,headers=headers)
    if a.status_code==200:
        return a.text
    else:
        return None

def gethttphtml(url):
    if not url.startswith("http://"):
        url=r"http://"+url
    a=requests.get(url)
    return a.status_code

def gethttpshtml(url):
    if  not url.startswith("https://"):
        url=r"https://"+url
    a=requests.get(url)
    return a.status_code

def getmode(url):
# 判断网站协议类型n为偶数为http/奇数为https
    while 1:
        n=0
        if (n%2==0):
            a=gethttphtml(url)
        else:
            a=gethttpshtml(url)
        if a!=404:
            break
        n=n+1
    if (n%2==0):
        print('目标未加密')
        mode='http://' 
    else:
        print('目标以加密')
        mode='https://' 
    return mode

if __name__ == "__main__":
    FeedManual='http://www.xiaoshuowu.com'
    Worm='*'
    Feed='http://www.xiaoshuowu.com/html/844/844878/'
    A=RobotsGetIsOk(Feed,Worm)
    print("爬虫:{0}".format(Worm),end="\t")
    print("种子:{0}".format(Feed))
    print("是否爬取：{0}".format(A))

