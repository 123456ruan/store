import  pymysql
host = "localhost"
user = "root"
password = "123456"
database = "bank"


# 修改
def update(sql,param):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()
    cursor.execute(sql,param)
    con.commit()
    cursor.close()
    con.close()
# 查询
def select(sql,param):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()
    cursor.execute(sql,param)
    return cursor.fetchall()
    cursor.close()
    con.close()
def select2(sql,param):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()
    return cursor.execute(sql,param)
    cursor.close()
    con.close()

