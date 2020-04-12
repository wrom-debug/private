import pymysql
str={'Ranking': '1', 'jpg': 'https://p0.meituan.net/movie/ce4da3e03e655b5b88ed31b5cd7896cf62472.jpg@160w_220h_1e_1c', 'name': '霸王别姬', 'actor': '主演：张国荣,张丰毅,巩俐', 'release time': '上映时间：1993-07-26', 'score': '9.5'}
name="郑吒"
# 链接数据库
db=pymysql.connect( host='127.0.0.1',
                    port=3306,
                    user='root',
                    password='123456',
                    database='wromdb',
                    charset='utf8'
)
# 创建游标对象
c=db.cursor()
# 游标方法
"""sql="select * from workdb where name=%s;"
c.execute(sql,[name])
a=c.fetchall()
print(a)"""
# 传递参数构造sql语句，并通过游标的execute方法运行，将查询到的对象使用fetall方法返回记录,读取是不需要提交和异常处理的
"""name="allen"
score="95.3"
try:
    sql = f"insert into stu (name,score) value (%s,%s);"
    c.execute(sql,[name,score])
# 提交数据库
    db.commit()
#     只有在记录进行写操作时需要提交数据库，与异常处理
except Exception as e:
    print(e)
    db.rollback()
#     出现异常进行数据库回滚"""
# 写入操作都是这个模板
# 关闭游标
c.close()
# 关闭数据库
db.close()