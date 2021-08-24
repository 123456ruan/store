import xlrd
import pymysql
host = "localhost"
user = "root"
password = "123456"
database = "sales"
exit = ['January_1','February_2','March_3','April_4','May_5','June_6','July_7','August_8','September_9','October_10', 'November_11','December_12' ]
wd = xlrd.open_workbook(filename=r"D:\python自动化测试1\python\day07\2020年每个月的销售情况.xlsx")
con = pymysql.connect(host=host, user=user, password=password, database=database)
cursor = con.cursor()
for i in exit:
    sql = "CREATE TABLE "+ i +"(`日期` VARCHAR(20) COLLATE utf8_bin DEFAULT NULL,`服装名称` VARCHAR(20) COLLATE utf8_bin DEFAULT NULL,`价格/件` FLOAT(10) DEFAULT NULL,`本月库存数量` FLOAT(10) DEFAULT NULL,`销售量/每日` FLOAT(10) DEFAULT NULL) ENGINE=INNODB DEFAULT CHARSET=utf8 COLLATE=utf8_bin"
    cursor.execute(sql)
    st = wd.sheet_by_name(i)
    for j in range(1,st.nrows):
        param = st.row_values(j)
        sql1 = "insert into " + i + " values(%s,%s,%s,%s,%s)"
        cursor.execute(sql1,param)
        con.commit()
cursor.close()
con.close()
print("完成导入")

