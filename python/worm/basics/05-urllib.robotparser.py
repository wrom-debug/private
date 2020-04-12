import urllib.robotparser
#user-agent:爬虫名称
# Disallow:禁止爬取的路径
# Allow:允许的路径
rp=urllib.robotparser.RobotFileParser()
rp.set_url("https://www.jd.com/robots.txt")
# 设置url，也可以在生成实例时设定
rp.read()
# 读取分析robots.txt
can=rp.can_fetch("*","https://www.jd.com")
print(can)
# 可以通过can_fetch（爬虫名称，需要爬取的url）返回的bool值判断url是否可爬
# 也可以省略ser_url与read使用parse（robots.txt的str）
time=rp.mtime()
print(time)
# 返回上一次爬取的时间