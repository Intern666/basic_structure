import pymysql
import app
# 1、创建连接
db = pymysql.connect(
    host="localhost",
    port=3306,
    db="nddb",
    user="root",
    password="root",
    charset="utf8"
)
# 2.创建游标对象
cursor = db.cursor()

user = app.User()
# 3.创建sql语句
# sql ="insert into myuser value('xiaoming','123')"
# rows = cls.execute(sql)
sql = "insert into Users(USER_NAME, USER_PWD) value(null,%s,%s)"
try:
    cursor.execute(sql, [user.name, user.pwd])
    db.commit()
    optSuccess = 1
except:
    db.rollback()
    optSuccess = 0
# 5.关闭
db.close()