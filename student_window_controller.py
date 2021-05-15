# -*- coding: utf-8 -*-
# !/usr/bin/env python
import psycopg2
from PyQt5 import QtWidgets

import filler
import sql
from student_window import Ui_Dialog as student_lk
import user_info
import datetime


class Student_window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = student_lk()
        self.ui.setupUi(self)
        self.setWindowTitle("Teacher window")
        # if user_info.admin :
        #     self.ui.admin_menu_button.clicked.connect(self.admin_menu_button_clicked)
        # else:
        #     self.ui.admin_menu_button.setVisible(False)
        self.db = sql.Sql()
        self.db.cursor.execute("SELECT id From people where user_id= '" + str(user_info.current_userID) + "'")
        student_id_list = self.db.cursor.fetchone()
        self.student_id = student_id_list[0]
        self.setInitialValues()


        self.ui.teacherNameComboBox.currentIndexChanged.connect(self.studentName_changed)
        self.ui.SubjectComboBox.currentIndexChanged.connect(self.studentName_changed)


        self.show()



    def studentName_changed(self):
        teacher_name = str(self.ui.teacherNameComboBox.currentText())
        subject_name = str(self.ui.SubjectComboBox.currentText())

        if self.ui.teacherNameComboBox.currentIndex() == 0 and self.ui.SubjectComboBox.currentIndex() == 0:

            self.db.cursor.execute("SELECT s.name, t.name, value, date from marks "
                                   "left join people st on MARKS.STUDENT_ID = st.ID"
                                   " left join people t on MARKS.TEACHER_ID = t.id "
                                   "left join subject s on MARKS.SUBJECT_ID = s.id "
                                   "where student_id = '{}'".format(self.student_id))
            filler.fillTable(self.ui.marksTableWidget, self.db.cursor, 4)

        elif self.ui.SubjectComboBox.currentIndex() == 0:
            self.db.cursor.execute("SELECT  s.name, t.name, value, date from marks "
                                   "left join people st on MARKS.STUDENT_ID = st.ID"
                                   " left join people t on MARKS.TEACHER_ID = t.id "
                                   "left join subject s on MARKS.SUBJECT_ID = s.id"
                                   " where t.name = '{}' and student_id = '{}'".format(teacher_name, self.student_id))
            filler.fillTable(self.ui.marksTableWidget, self.db.cursor, 4)
        elif self.ui.teacherNameComboBox.currentIndex() == 0:
            self.db.cursor.execute("SELECT  s.name, t.name, value, date from marks "
                                   "left join people st on MARKS.STUDENT_ID = st.ID"
                                   " left join people t on MARKS.TEACHER_ID = t.id "
                                   "left join subject s on MARKS.SUBJECT_ID = s.id"
                                   " where s.name = '{}' and student_id = '{}'".format(subject_name, self.student_id))
            filler.fillTable(self.ui.marksTableWidget, self.db.cursor, 4)
        else:
            self.db.cursor.execute("SELECT s.name, t.name, value, date from marks "
                                   "left join people st on MARKS.STUDENT_ID = st.ID"
                                   " left join people t on MARKS.TEACHER_ID = t.id "
                                   "left join subject s on MARKS.SUBJECT_ID = s.id"
                                   " where t.name = '{}' and s.name = '{}' and student_id = '{}'".format(teacher_name, subject_name, self.student_id))
            filler.fillTable(self.ui.marksTableWidget, self.db.cursor, 4)


    def setInitialValues(self):
        user_id = user_info.current_userID
        self.db.cursor.execute("SELECT name From people where user_id= '" + str(user_id) + "'")
        student_name_list = self.db.cursor.fetchone()
        self.ui.name_label.setText(str(student_name_list[0]))

        # self.db.cursor.execute("SELECT name from groups")
        # filler.fillComboBox(self.ui.groupComboBox, self.db.cursor)

        self.db.cursor.execute("SELECT name From people where type = 'P' ")
        filler.fillComboBox(self.ui.teacherNameComboBox, self.db.cursor)


        filler.fillMultipleComboBox([self.ui.SubjectComboBox], self.db.cursor, 'SELECT name from subject')
        self.db.cursor.execute("SELECT  s.name, t.name, value, date from marks "
                               "left join people st on MARKS.STUDENT_ID = st.ID"
                               " left join people t on MARKS.TEACHER_ID = t.id "
                               "left join subject s on MARKS.SUBJECT_ID = s.id where student_id = {}".format(self.student_id))
        filler.fillTable(self.ui.marksTableWidget, self.db.cursor, 4)
