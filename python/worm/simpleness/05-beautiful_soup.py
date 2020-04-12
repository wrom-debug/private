from bs4 import BeautifulSoup
html="""
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!--ELsie--></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup=BeautifulSoup(html,"lxml")
# print(soup.prettify())
print(soup.title.string)
# 将html片段使用BeautifulSoup方法初始化使用lxml解析器类型传给soup，在初始化时会对不完整的部分进行填补
# prettify方法返回正常缩进的格式
# string返回选择节点的文本内容
print(soup.p)
print(type(soup.p))
# 本方式选择节点只会返回第一个匹配的节点
print(soup.a.name)
# name属性返回节点名称
print(soup.a.attrs)
# attrs返回所有属性以字典形式
print(soup.a['href'])
# 也可以使用这种方式获取节点的属性值
print(soup.html.a['href'])
#也可以嵌套选择节点