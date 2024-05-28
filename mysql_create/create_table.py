import pymysql


class DatabaseOperation(object):

    def __init__(self, ip, user, pwd, database, charset="utf8", port=3306):
        conn = pymysql.connect(host=ip, password=pwd, database=database, user=user, charset=charset, port=port)
        self.conn = conn
        pass

    def creat_table(self, table_name=None, fiels=None, primary_key="id"):
        """
        创建数据表调用时，需注意fiels为字典，key为字段名，value为字段类型和限制条件如：fiels={"id": "INT UNSIGNED AUTO_INCREMENT", "one": "int(12)", "two": "VARCHAR(100) NOT NULL"}
        table_name参数意如其名，数据表的名字
        primary_key字段为要设置的主键，默认为id（这个字段需要存在才能设置主键为id）
        """
        num = 0
        fiel_data = ""
        for key, value in fiels.items():
            num += 1

            if num == 1:
                fiel_data += key + " " + value + ","

            else:
                fiel_data += key + " " + value + ","

        sql = "CREATE TABLE IF NOT EXISTS %s(%s PRIMARY KEY ( `%s` ));" % (table_name, fiel_data, primary_key)
        curs = self.conn.cursor()
        curs.execute(sql)
        print("数据表添加成功。")

    def insert(self, table_name, need_insert_fiels_and_data=None):
        """need_insert_fiels_and_data: 这个参数是字典,字段是key，值是value"""

        need_insert_keys = " "
        need_insert_values = " "
        run_for_tage = 0

        for key, value in need_insert_fiels_and_data.items():
            run_for_tage += 1

            if run_for_tage == len(need_insert_fiels_and_data):
                need_insert_keys += "%s" % key
                if type(value) == int:
                    need_insert_values += "%s" % value
                elif type(value) == str:
                    need_insert_values += "'%s'" % value
                elif type(value) == bool:
                    need_insert_values += "%s" % value
                else:
                    need_insert_values += "'%s'" % value

            else:
                need_insert_keys += "%s, " % key
                if type(value) == int:
                    need_insert_values += "%s, " % value
                elif type(value) == str:
                    need_insert_values += "'%s', " % value
                elif type(value) == bool:
                    need_insert_values += "%s, " % value
                else:
                    need_insert_values += "'%s', " % value

        sql = "insert into %s (%s) values (%s);" % (table_name, need_insert_keys, need_insert_values)
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()

    def close_db(self):
        self.conn.close()

    # 我们写下一个SQL插入语句，并尝试执行它。如果操作成功.使用commit来修改
    def commit_option(self):
        self.conn.commit()

    # def __del__(self):
    #     self.conn.commit()
    #     self.conn.close()

    # 执行过程中发生错误,通过回滚来撤销修改
    def rollback(self):
        self.conn.rollback()

    def truncate(self, table):
        sql = "truncate table %s" % table
        self.conn.cursor().execute(sql)



fiels = {"id": "INT(10) UNSIGNED AUTO_INCREMENT",
         "phone": "varchar(250) NOT NULL",
         "phone_decode": "varchar(250) NOT NULL",
         "phone_user":"varchar(250) NOT NULL",
         "borrow_in_people":"varchar(250) NOT NULL",
         "borrow_date":"varchar(250) NOT NULL",
         "is_return":"varchar(250) NOT NULL",
         "return_date":"varchar(250) NOT NULL",
         "borrow_out_people":"varchar(250) NOT NULL",
         "remark":"varchar(250) NOT NULL",
         }
# fiels = {
#         "id": "INT(10) UNSIGNED AUTO_INCREMENT",
#          "phone": "varchar(250) NOT NULL",
# }
cnn = DatabaseOperation(ip="43.138.135.38", pwd="123456789", user="root", database="web")
# cnn.truncate("computer_infos")
cnn.creat_table("phone_info", fiels)