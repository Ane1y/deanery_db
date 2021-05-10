from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLineEdit

import user_info
from sign_in import Ui_Dialog as loginmain
from teacher_window_controller import Teacher_window
#from student_window_controller import Student_window
import sql


class sign_inWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = loginmain()
        self.ui.setupUi(self)
        self.setWindowTitle("����")
        self.ui.sign_in_button.clicked.connect(self.sign_in_button_clicked)
        #self.ui.sign_up_button.clicked.connect(self.sign_up_button_clicked)
        self.ui.password_lineEdit.setEchoMode(QLineEdit.Password)

        self.db = sql.Sql()

    def sign_in_button_clicked(self):
        l = self.ui.phone_lineEdit.text()
        p = self.ui.password_lineEdit.text()
        if (l.strip() == ''):
            message = "������� ����� ��������"
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setModal(True)
            error_message.setWindowTitle("������ �����")
            error_message.showMessage(message)
            if len(l) != 0:
                self.ui.phone_lineEdit.clear()
            self.ui.password_lineEdit.clear()
        elif (p.strip() == ''):
            message = "������ �� ������. ���������� ��� ���!"
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setModal(True)
            error_message.setWindowTitle("������ �����")
            error_message.showMessage(message)
            if len(p) != 0:
                self.ui.password_lineEdit.clear()

        elif not(l.isdecimal()):

            message = "������������ ������ � ���� ������. ��������� ������������ ������ � ��������� ����."
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setModal(True)
            error_message.setWindowTitle("������ �����")
            error_message.showMessage(message)
            self.ui.phone_lineEdit.clear()
            self.ui.password_lineEdit.clear()

        elif (p.find(' ') != -1):
            message = "������� ������������ �� ���������� ��� ������ �������� ������! ��������� ������������ ������ � ��������� ����."
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setModal(True)
            error_message.setWindowTitle("������ �����")
            error_message.showMessage(message)
            self.ui.password_lineEdit.clear()

        else: # ���� ������ ��� �������� �������� �������� ������������ �� ��
            status, role, id = self.db.checkPassword(l, p)
            if (status == False):
                message = "�� ������ ������������ � ����� �������/�������"
                error_message = QtWidgets.QErrorMessage(self)
                error_message.setModal(True)
                error_message.setWindowTitle("������ �����")
                error_message.showMessage(message)
                self.ui.password_lineEdit.clear()
            else:
                user_info.current_role = role
                user_info.current_userID = id
                if user_info.current_role == "physician":
                    #TODO: ���������� �������� �� ������
                    self.db.cursor.execute("SELECT type from people where user_id = %s", str(id))
                    role_id = self.db.cursor.fetchone()
                    if role_id[0] == 2:
                        user_info.admin = True
                    self.menu = Teacher_window()
                # else:
                #      self.menu = Student_window()
                self.close()
                self.menu.show()

