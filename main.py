import sys

from PyQt5 import QtWidgets
#from sign_in_controller import sign_inWindow
from sql import Sql
from teacher_window_controller import Teacher_window



if __name__ == '__main__':
    db = Sql()

    app = QtWidgets.QApplication([])
    # window = Admin_Controller()
    window = Teacher_window()
    window.show()
    db.cnxn.close()
    sys.exit(app.exec())

    # def checkPassword(self, login, password):
    #     cipher = Fernet(user_info.cipher_key)
    #     temp = "(SELECT id from authentication_data WHERE phone = '" + login + "')"
    #     self.cursor.execute("SELECT id, password, CASE " \
    #         "when exists (select true from physicians where user_id = " + temp + ") then 'physician' " \
    #         "when exists (select true from patients where user_id = " + temp + ") then 'patient' " \
    #         "ELSE '0' " \
    #         "END FROM authentication_data WHERE phone = '" + login + "'")
    #     row = self.cursor.fetchone()
    #     if row is not None:
    #         passw = cipher.decrypt(str.encode(row[1])).decode('utf8')
    #         if password == passw:
    #             return True, row[2], row[0]
    #         else:
    #             return False, row[2], row[0]
    #     else:
    #         return False, 0, 0