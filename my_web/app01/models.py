from django.db import models
import pymysql as mysql
# Create your models here.

def select_computer_info():
    # 创建数据库连接对象
    db = mysql.connect("10.32.71.66", "root", "123456789", "mysql", port=3306, charset='utf8')