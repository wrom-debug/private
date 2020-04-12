#liunx基础使用
[toc]
##基础
命令行构成:
~~~
用户@计算机名：路径$
~~~
修改除home目录下以外的文件需要管理员身份运行(运行是需要输入管理员密码)
~~~
sudo 命令
~~~
ctrl+l键清空终端显示
命令|作用
---|:--:
cd|切换目录（可以使用绝对路径（/根目录下的路径）也可以使用相对路径（.代表当前目录  ..代表当前目录的上级目录））
ls    ls -l    ls -a|内容当前路径下的文件 -l 查看详细内容 -a 查看隐藏文件（以点开头的文件）
cp [-r]原文件 复制的路进|复制文件 [-r] 复制路径
vm 原文件 路径|移动文件
rm 文件|删除文件[-r]删除路径
mkdir 文件夹名称|创建文件夹[-p]创建路进下文件夹
rmdir 文件夹名称|删除空文件夹
touch 文件名称|创建文件
cat 文件名称|查看文件内容

##软件管理
命令|作用
---|:--:
sudo apt- get update|更新软件包
sudo apt-get install 软件名称|安装软件
sudo apt-get remove --purge 软件名|卸载软件

##ssh服务
命令|作用
---|:--:
sudo service ssh start/restart/stop|启动/重启/停止ssh服务
ssh-keygen|生成ssh密钥对在用户下.ssh文件夹下（rsa的私钥 rsa.pub公钥）

##解压




