import  re

content="Hello 123 4567 World_this is a Regex Demo" \
        "Hello 123 4567 World_this is a Regex Demo"
print(len(content))
r=re.match(('^Hello\s\d\d\d\s\d{4}\s\w{10}'),content)
print(r)
print(r.group())
print(r.span())
# match方法需要传入re语法，需匹配的字符串
# 返回这这个Match对象，其span方法返回匹配字符在总字符的的位置，geoup方法返回匹配的字符，但只会匹配第一个匹配的字符
r1=re.match(('^Hello\s(\d\d\d)\s(\d{4})\s\w{10}'),content,re.S)
print(r1)
print(r1.group(1))
print(r1.span())
# 在group方法中传入数字可以选定地几个小括号
r2=re.search(('\s(\d\d\d)\s(\d{4})\s\w{10}'),content,re.S)
print(r2)
print(r2.group(1))
print(r2.span())
# search是对match的加强，会返回地一个匹配的字符，不想match要冲头匹配
r3=re.findall(('\s(\d\d\d)\s(\d{4})\s\w{10}'),content,re.S)
print(r3)
# 查询全部内容并输出由元组构成元素的列表
r4=re.sub('\s(\d\d\d)\s(\d{4})\s\w{10}',"",content,re.S)
print(r4)
# sub可以将正则匹配的内容用指定内容替换
r5=re.compile('\s(\d\d\d)\s(\d{4})\s\w{10}')
# compile可以将正则构建对象，可以在其中传入修饰符，之后使用时就可以省略了


