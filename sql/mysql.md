#SQL
[toc]
###安装myqsl
~~~
sudo apt-get install mysql-server
sudo apt-get install mysql-client
~~~
可以在/etc/mysql/debian.cnf中查看默认账户密码
###myql的一般操作
~~~
service mysql start     #启动
service mysql stop      #停止
service mysql restart       #重启
~~~
###登录
~~~
mysql -h地址 -u账户 -p密码
~~~
###修改默认帐号和密码
~~~
mysql> update mysql.user set authentication_string=password('new passwd') where user='root' and Host ='localhost';
~~~
##数据库操作
###查看数据库
~~~
show databases;
~~~
###创建数据库
创建名为wormdb的数据库，编码格式为utf-8
~~~
create database wormdb charset=utf8;
~~~
###查看数据库u编码格式
查看wormdb的编码格式
~~~
shuow create database wormdb;
~~~
###查看当前所在库
~~~
select database();
~~~
###切换库
切换至wormdb库
~~~
use wormdb;
~~~
###删除库
~~~
drop database wormdb;
~~~
##表操作
###添加表

~~~
create table maoyan_1 (列内容 );
~~~
###查看数据库中的表
~~~
show tables;
~~~
###查看表的列结构
~~~
desc 表名;
~~~
###删除表
~~~
drop table 表名;
~~~
###查看表构成（可以查看编码格式，数据库引擎，列字段）
~~~
show create table 表名
~~~
###删除表
~~~
drop table 表名;
~~~
##记录操作
###插入
~~~
insert into 表名(字段1，......)values(值1,....);
insert into 表名 values (值1),(值2);
~~~
###查询
~~~
select 列表名 from 表名 [where 条件];
select * from 表名 [where 条件];
~~~
###更新
~~~
update 表名 set 字段=值;
~~~
###删除
~~~
delete from 表名 where 条件;
~~~
##字段操作
###添加
~~~
alter table 表名 add 字段 类型;     #在最后添加
alter  table 表名 add 字段 类型 first;      #在开头添加
alter  table 表名 add 字段 类型 after 字段;     #在字段后添加
~~~
###删除
~~~
alter table 表名 drop 字段名;
~~~
###修改字段类型
~~~
alter table 表名 modify 字段名 新类型
~~~
###修改字段
~~~
alter table 表名 change 旧字段  新字段 类型
~~~
###重命名表
~~~
alter table 旧表名 rename 新表名
~~~
##高级搜索
###模糊匹配
~~~
select 字段 form 表名 where 字段 like 条件
~~~
模糊查询用%代替任何字符
条件可以为正则表达式
###排序
~~~
selcet 字段 from 表名 where 条件 order by 字段 [ASC/DESC]
~~~
ASC：升序
DESC：降序
###分页
~~~
select 字段 from  表名 where 条件 limit 数量
~~~
显示多少条
###联合查询
~~~
select 字段 from 表名 where 条件 union [all] select 字段 from 表名 where 条件
~~~
all，将重复的记录重复显示

两次查询的显示字段要一样
###多表查询
~~~
select 表名.字段 from 表名 where 条件
~~~
##数据库备份
在命令行中输入
###备份
~~~
mysqldump -u用户名 -p 数据库名称 >路径.sql
~~~
###导入
~~~
mysql -u用户名 -p可以名称 < 库路径.sql
~~~
