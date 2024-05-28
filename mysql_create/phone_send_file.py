import xlrd
import os
import datetime
from mysql_create.create_table import DatabaseOperation
class PHONESENDFILE():
    """
    1.创建数据表以及导入数据
    2.发送信息到对应的群
    """

    def __init__(self):
        super(PHONESENDFILE, self).__init__()


# 创建数据表以及导入数据
    def create_info(self):
        cnn = DatabaseOperation(ip="43.138.135.38", pwd="123456789", user="root", database="web")
        cnn.truncate("phone_info")  # 需要清空表从新存储数据，因为机器名字可能会修改，导致与数据库中的名字不一样
        for lis_info in self.xlsx_file():
            phone_info_dict = dict()
            phone_info_dict["phone"] = lis_info[0]
            phone_info_dict["phone_decode"] = lis_info[1]
            phone_info_dict["phone_user"] = lis_info[2]
            phone_info_dict["borrow_in_people"] = lis_info[3]
            phone_info_dict["borrow_date"] = self.covert_time(lis_info[4])
            phone_info_dict["is_return"] = lis_info[5]
            phone_info_dict["return_date"] = lis_info[6]
            phone_info_dict["borrow_out_people"] = lis_info[7]
            phone_info_dict["remark"] = lis_info[-1]
            print(type(phone_info_dict), phone_info_dict)
            cnn.insert(table_name="phone_info", need_insert_fiels_and_data=phone_info_dict)
        cnn.close_db()
        return True

    # excel中的时间转换
    def covert_time(self, time_int):
        """
        time_int:excel转换的时间戳
        """
        if time_int is "":
            return time_int
        else:
            py_date = datetime.date.fromordinal(datetime.datetime(1900, 1, 1).toordinal() + int(time_int) - 2)
            py_date_str = py_date.strftime('%Y-%m-%d')

            return py_date_str

    @staticmethod
    def xlsx_file():
        file_list = []
        # workspeace = os.getenv("WorkSpace")
        workspeace = r"E:\构建手机设备管理.xlsx"
        # file_path = os.path.abspath(os.path.join(workspeace, "Buildphone.xlsx"))
        data_file = xlrd.open_workbook(workspeace)
        sheet = data_file.sheets()[0]

        for row_index in range(sheet.nrows):
            if row_index != 0:
                row = sheet.row_values(row_index)
                file_list.append(row)

        return file_list



PHONESENDFILE().create_info()