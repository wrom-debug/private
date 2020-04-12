from lxml import etree

"""text=
        <div>
        <ul>
        <li class="item-0"><a href="link1.html">first item </a></li>
        <li class="item-1"><a href="link2.html">second item </a></li>
        <li class="item-inactive"><a href="link3.html">third item </a></li>
        <li class="item-1"><a href="link4.html">fourth item </a></li>
        <li class="item-0"><a href="link5.html">fifth item </a>
        </ul>
        </div>

html=etree.HTML(text)
result=etree.tostring(html)"""
# print(result.decode('utf-8'))
# HTML方法将字符串转化成html对象，tostring方法将html对象转换成str字符串，并使用utf-8格式输出
"""html=etree.parse("./test.html",etree.HTMLParser())
result=etree.tostring(html)
print(result.decode('utf-8'))
r=html.xpath("//li")
result=etree.tostring(r[2])
print(result.decode('utf-8'))"""
# 使用parse方法可以打开文件，在传入HTMLParser与HTML传入字符串一样
# 再使用xpath进行全部匹配，可以再用tostring转化为字符串
"""r=html.xpath('//li/a[@href="link5.html"]/text()')
print(r)"""
# [@]可以使用该方法指定匹配的节点的属性/text（）方法可以匹配节点的文本
# 本例匹配的是li节点下的a节点其中属性为href="link5.html"的文本内容
"""r=html.xpath('//li/a/@href')
print(r)"""
# 也可使用该格式获得节点的属性值
text="""
<li class="li li-first" name="item"><a href="link.html">fifth item </a>
"""
html=etree.HTML(text)
r=html.xpath('//li[contains(@class,"li")]/a/text()')
print(r)
# 面对一个属性有多个值时使用contains传入属性与包含的值即可
r=html.xpath('//li[contains(@class,"li") and @name="item"]/a/text()')
print(r)
# 节点有多个属性时可以使用该方法定位
html=etree.parse("./test.html",etree.HTMLParser())
r=html.xpath('//li[last()]/a/text()')
print(r)
r=html.xpath('//li[last()-1]/a/text()')
print(r)
r=html.xpath('//li[position()<4]/a/text()')
print(r)
# 可以在节点中添加序号来匹配第几个节点
# 其中last（）表示到序，position（）表示自身序号.
r=html.xpath('//li[1]/ancestor::*')
print(r)
r=html.xpath('//li[1]/attribute::*')
print(r)
r=html.xpath('//li[1]/child::*')
print(r)
r=html.xpath('//li[1]/descendant::*')
print(r)
r=html.xpath('//li[1]/following::*')
print(r)
r=html.xpath('//li[1]/following-sibling::*')
print(r)
# ancestor::选取祖先辈节点
# attribute::节点的属性值
# child::选取子节点
# descendant::选取子孙节点
# following::选取之前选中的节点之之后的内容，及li[1]的</li>后的所有节点
# following-sibling::选取除本节点的所有兄弟节点