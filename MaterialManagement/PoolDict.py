import pymysql as mysql

def connectionPolling():

    db=mysql.connect(host="localhost",port=3306,user="root",password='123',db="mm")
    cmd=db.cursor(mysql.cursors.DictCursor)
    return (db,cmd)



