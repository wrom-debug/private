import urllib.parse


result=urllib.parse.urlparse("http://www.baodu.com/index.html;user?id=5#comment")
print(result)
# 使用urlparse类来分析url内容 scheme协议 netloc域名 path访问路径 paeams参数 query查询条件 fragment锚点
# urlparse（urlstring，scheme=“”，allow——fragments=True）
# urlstring带解析的url scheme默认的协议（只有在url中没有表明使用）all_fragments忽略锚点（设置成False忽略）
# 可以使用索引获得result的指定属性 或者result.scheme来获取
data=['http', 'www.baodu.com', 'index.html', 'user', 'id=5', 'comment']
url=urllib.parse.urlunparse(data)
print(url)
# urlparse是分解url，相对的urlunparse就是并接成url，传入长度6元素的数据
# urlsplit就是urlparse没有paeams将其合并到path中
# urlunsplit相当于urlunparse不过传入数据必须长度为5个元素
# urljoin（基础url，新rul）会将新url的内容拼接到基础url上，基础url只为新url提供scheme协议 netloc域名 path访问路径
# 但当新url中有这些内容时就使用新url的
data={"name":"a","age":"18"}
bas_url="http://www.baodu.com?"
new_url=bas_url+urllib.parse.urlencode(data)
print(new_url)
# urlencode将字典构造到url中
# parse_qs就是urlencode的反序转换回字典
# parse_qsl与parse_qs一样只不过输出元组列表

# quote将内容转换为url的编码格式
# unquote将url编码

