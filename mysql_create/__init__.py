# 一些常用的mysql命令
# 常见命令
# show databases; 查看所有数据库
# use 数据库名；使用该数据库库
# select database(); 查看当前数据库的名称
# create database 数据库名；创建数据库
# 1.连接数据库
# 1.1.连接自己的机器上的mysq
# mysql -u root -p
# 1.2.连接其他数据库上的mysql
# mysql -h 所连接机器的ip -u root -p

# 2.查询
# 2.1.select database(); 查看当前数据库的名称
# 2.2.use 数据库名；使用该数据库库
# 2.3.show tables; 查看该数据库中的所有表格
# 2.4.desc 表名；查看表的结构类型

# PyMySQL操作mysql步骤
# import  pymysql
# 连接数据库
# conn=pymysql.connect(host='localhost',user='ian',password='ian123',database='ian',charset='utf8')
# 创建游标
# cur=con.cursor()
# 生成数据库
# sql='select * from tb_test'
# #获取结果
# cur.execute(sql)
# # 获取所有记录  fetchall--获取所有记录   fetchmany--获取多条记录，需传参  fetchone--获取一条记录
# all=cur.fetchall()
# # 输出查询结果
# print(all)
# 我们写下一个SQL插入语句，并尝试执行它。如果操作成功.使用commit来修改
# conn.commit()
# 执行过程中发生错误,通过回滚来撤销修改
# conn.rollback()
# # 关闭游标
# cur.close()
# # 关闭数据库连接，目的为了释放内存
# conn.close()