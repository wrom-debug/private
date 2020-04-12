#-*- coding=utf-8 -*-
'''
#1.1
print("人生苦短，我用python")
#1.1.1
print("--<-<-<e")
#1.1.2
print("要么出众，要么出局")
#1.1.3
print("(=^ ^=)")
#1.1.4
a="\t滁州西涧\n独怜幽草涧边生，上有黄鹂深树鸣。\n春潮带雨晚来急，野渡无人舟自横。"
print(a)
#1.2
height=1.70
print("你的身高：{0}".format(str(height)))
weight=48.5
print("你的体重：{0}".format(str(weight)))
bim=weight/(height**2)
print("你的BMI指数为：{0}".format(str(bim)))
if bim<18.5:
    print("轻")
if bim>=18.5 and bim<24.9:    
    print("正常")
if 29.9>bim>=24.9:
    print("重")
if bim>29.9:
    print("肥胖")
#1.2.1
money_all=56.75+72.91+88.50+26.37+68.51
print("总价：{0}".format(str(money_all)))
print("应收：{0}".format(str(int(money_all))))
#1.2.2
a=95
b=92
c=89
sub=max(a,b,c)-min(a,b,c)
print("fc:{0}".format(str(sub)))
print("pjf:{0}".format(str((a+b+c)/3)))
#2.7.1
a=input("欢迎使用xxx充值业务，请输入充值金额：")
print("充值成功，您本次充值{0}元".format(a))

#2.7.2
f=float(input("请输入父亲身高："))
m=float(input("请输入母亲身高："))
print("预计儿子身高：{0}".format(str((f+m)*0.54)))

#2.7.3
bs=int(input("请输入步数："))
print("消耗卡路里：{0}".format(str(bs*28)))

#3.7.1
a=10
while a!=0:
    a=int(input("按0退出,按1-5查询"))
    if 6>a>0:
        print("200g")

#3.7.2

import random
b=0
a=random.randint(a=1,b=10)
while b!=a:
    b=int(input())
    if a>b:
        print("max")
    if a<b:
        print("min")
print("正确就是{0}".format(str(a)))

#3.7.3
b=0
while b<4:
    b=int(input("1-3:"))
    if b==1:
        print(b+11)
    if b==2:
        print(b+22)
    if b==3:
        print(b+33)

#4.7.1
a={"tx":[1,2,3,4],"ss":[5,6,7,8,9]}
b=list(a.keys())
for i in b:
    print(i+":")
    print(a.get(i))

#4.7.3
d=[("a",5),("b",7),("c",6)]
a=[5,7,6]
a.sort()
print(a)
for c in a:
    for i in d:
        if i[1]==c:
            print(i)
       
'''
#