# -*- coding: utf-8 -*-
# !/usr/bin/env python
import psycopg2
from PyQt5 import QtWidgets

import filler
import sql
from user_info import current_userID as teacher_id
from teacher_window import Ui_Dialog as teacher_lk
import user_info
import datetime

class Teacher_window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = teacher_lk()
        self.ui.setupUi(self)
        self.setWindowTitle("Teacher window")
        # if user_info.admin :
        #     self.ui.admin_menu_button.clicked.connect(self.admin_menu_button_clicked)
        # else:
        #     self.ui.admin_menu_button.setVisible(False)
        self.db = sql.Sql()

        self.setInitialValues()

        self.ui.numGroupsWIthMarksButton.clicked.connect(self.numGroupsWIthMarksClicked)
        self.ui.addUserPushButton.clicked.connect(self.addUserClicked)
        self.ui.studentNameComboBox.currentIndexChanged.connect(self.studentName_changed)
        self.ui.teacherNameComboBox.currentIndexChanged.connect(self.studentName_changed)
        self.ui.SubjectComboBox.currentIndexChanged.connect(self.studentName_changed)
        self.ui.addMarkPushButton.clicked.connect(self.addMarkClicked)
        self.ui.copyGroupButton.clicked.connect(self.copyGroupClicked)
        self.ui.turnGroupBackButton.clicked.connect(self.turnGroupBackClicked)
        self.ui.yearComboBox.currentIndexChanged.connect(self.yearChanged)
        self.show()
        self.ui.avgMarksInIntervalButton.clicked.connect(self.avgMarksInIntervalClicked)
        self.ui.saveIntervalButton.clicked.connect(self.saveIntervalClicked)

    def avgMarksInIntervalClicked(self):
        beginDate = self.ui.beginDateEdit.date()
        endDate = self.ui.endDateEdit.date()
        beginDate  = beginDate.toString("yyyy-MM-dd")
        endDate = endDate.toString("yyyy-MM-dd")

        self.db.cursor.execute("select s.name, round(avg_marks, 3) from intervalAvgMarks('{}'::timestamp, '{}'::timestamp)"
                           "left join subject s on s.id = subject_id".format(beginDate, endDate))
        filler.fillTable(self.ui.yearSubjectTableWidget, self.db.cursor, 2)

    def saveIntervalClicked(self):
        beginDate = self.ui.beginDateEdit.date()
        endDate = self.ui.endDateEdit.date()
        beginDate  = beginDate.toString("yyyy-MM-dd")
        endDate = endDate.toString("yyyy-MM-dd")
        query = "select s.name, round(avg_marks, 3) from intervalAvgMarks('{}'::timestamp, '{}'::timestamp) " \
                "left join subject s on s.id = subject_id".format(beginDate, endDate)
        outputquery = "COPY ({}) TO STDOUT WITH CSV HEADER".format(query)
        with open('resultsfile.csv', 'w') as f:
            self.db.cursor.copy_expert(outputquery, f)



    def yearChanged(self):
        self.ui.yearSubjectTableWidget.clear()
        year = self.ui.yearComboBox.currentText()
        self.db.cursor.execute("select s.name, avg_marks from subjectsAndAvgMarkInOneYear('{}')"
                               "left join subject s on s.id = subject_id".format(year))
        filler.fillTable(self.ui.yearSubjectTableWidget, self.db.cursor, 2)


    def turnGroupBackClicked(self):
        number = list(self.ui.groupPointerComboBox2.currentText())
        new_number = number.copy()
        new_number[0] = str(int(new_number[0]) + 1)
        str_new_number = ''
        str_number = ''
        for i in new_number:
            str_new_number += i

        for i in number:
            str_number += i
        self.db.cursor.execute("Delete from people  WHERE group_id = (SELECT id from groups where name = '{}');"
                               "Delete from groups where name = '{}';".format(str_number, str_new_number))

        self.db.cnxn.commit()


    def copyGroupClicked(self):
        number = list(self.ui.groupPointerComboBox2.currentText())
        new_number = number.copy()
        new_number[0] = str(int(new_number[0]) + 1)
        str_new_number = ''
        str_number = ''
        for i in new_number :
            str_new_number += i

        for i in number:
            str_number += i
        self.db.cursor.execute("INSERT INTO groups (name) VALUES ('{}'); "
                               "INSERT INTO people (first_name, last_name, pather_name, group_id, type) "
                               "(SELECT  first_name, last_name, pather_name, (SELECT id from groups where name = '4084/1_2018'), type from people "
                               "WHERE group_id = (SELECT id from groups where name = '{}'));".format(str_new_number, str_number))

        self.db.cnxn.commit()

    def addMarkClicked(self):
        student_name = str(self.ui.studentNameComboBox.currentText())
        teacher_name = str(self.ui.teacherNameComboBox.currentText())
        subject_name = str(self.ui.SubjectComboBox.currentText())
        mark_value = str(self.ui.markSpinBox.value())
        self.db.cursor.execute("INSERT INTO marks (student_id, subject_id, teacher_id, value, date) "
                               "VALUES ((SELECT id from People WHERE name = '{}'), "
                               "(SELECT id from subject WHERE name = '{}'), "
                               "(SELECT id from people WHERE name = '{}'), "
                               "'{}', current_timestamp)".format(student_name, subject_name, teacher_name, mark_value))

        self.db.cnxn.commit()
        self.set_default_marks_table()


    def set_default_marks_table(self):
        self.db.cursor.execute("SELECT st.name, s.name, t.name, value, date from marks "
                               "left join people st on MARKS.STUDENT_ID = st.ID"
                               " left join people t on MARKS.TEACHER_ID = t.id "
                               "left join subject s on MARKS.SUBJECT_ID = s.id order by date desc")
        filler.fillTable(self.ui.marksTableWidget, self.db.cursor, 5)

    def studentName_changed(self):
        student_name = str(self.ui.studentNameComboBox.currentText())
        teacher_name = str(self.ui.teacherNameComboBox.currentText())
        subject_name = str(self.ui.SubjectComboBox.currentText())

        if self.ui.studentNameComboBox.currentIndex() == 0 and self.ui.teacherNameComboBox.currentIndex() == 0 and \
                self.ui.SubjectComboBox.currentIndex() == 0:
            self.set_default_marks_table()
        elif self.ui.studentNameComboBox.currentIndex() == 0 and self.ui.teacherNameComboBox.currentIndex() == 0:
            self.db.cursor.execute("SELECT st.name, s.name, t.name, value, date from marks "
                               "left join people st on MARKS.STUDENT_ID = st.ID"
                               " left join people t on MARKS.TEACHER_ID = t.id "
                               "left join subject s on MARKS.SUBJECT_ID = s.id "
                                   "where s.name = '{}'".format(subject_name))
            filler.fillTable(self.ui.marksTableWidget, self.db.cursor, 5)
        elif self.ui.teacherNameComboBox.currentIndex() == 0 and self.ui.SubjectComboBox.currentIndex() == 0:

            self.db.cursor.execute("SELECT st.name, s.name, t.name, value, date from marks "
                               "left join people st on MARKS.STUDENT_ID = st.ID"
                               " left join people t on MARKS.TEACHER_ID = t.id "
                               "left join subject s on MARKS.SUBJECT_ID = s.id "
                                   "where st.name = '{}'".format(student_name))
            filler.fillTable(self.ui.marksTableWidget, self.db.cursor, 5)
        elif self.ui.SubjectComboBox.currentIndex() == 0 and self.ui.studentNameComboBox.currentIndex() == 0 :
            self.db.cursor.execute("SELECT st.name, s.name, t.name, value, date from marks "
                               "left join people st on MARKS.STUDENT_ID = st.ID"
                               " left join people t on MARKS.TEACHER_ID = t.id "
                               "left join subject s on MARKS.SUBJECT_ID = s.id"
                                " where t.name = '{}'".format(teacher_name))
            filler.fillTable(self.ui.marksTableWidget, self.db.cursor, 5)
        elif self.ui.SubjectComboBox.currentIndex() == 0 and self.ui.teacherNameComboBox.currentIndex() == 0:
            self.db.cursor.execute("SELECT st.name, s.name, t.name, value, date from marks "
                               "left join people st on MARKS.STUDENT_ID = st.ID"
                               " left join people t on MARKS.TEACHER_ID = t.id "
                               "left join subject s on MARKS.SUBJECT_ID = s.id"
                                " where t.name = '{}'".format(student_name))
            filler.fillTable(self.ui.marksTableWidget, self.db.cursor, 5)

        elif self.ui.SubjectComboBox.currentIndex() == 0:
            self.db.cursor.execute("SELECT st.name, s.name, t.name, value, date from marks "
                               "left join people st on MARKS.STUDENT_ID = st.ID"
                               " left join people t on MARKS.TEACHER_ID = t.id "
                               "left join subject s on MARKS.SUBJECT_ID = s.id"
                                " where st.name = '{}' and t.name = '{}'".format(student_name, teacher_name))
            filler.fillTable(self.ui.marksTableWidget, self.db.cursor, 5)
        else:
            self.db.cursor.execute("SELECT st.name, s.name, t.name, value, date from marks "
                               "left join people st on MARKS.STUDENT_ID = st.ID"
                               " left join people t on MARKS.TEACHER_ID = t.id "
                               "left join subject s on MARKS.SUBJECT_ID = s.id"
                                " where t.name = '{}' and st.name = '{}' and s.name = '{}'".format(teacher_name,
                                                                                                   student_name, subject_name))
            filler.fillTable(self.ui.marksTableWidget, self.db.cursor, 5)
    def addUserClicked(self):
        first_name = str(self.ui.firstNameLineEdit.text())
        last_name = str(self.ui.lastNameLineEdit.text())
        pather_name = str(self.ui.patherNameLineEdit.text())
        group = str(self.ui.groupNumComboBox.currentText())
        type = str(self.ui.typeComboBox.currentText())
        self.db.cursor.execute("Select id from groups where name = '3084/2_2018'")
        number = self.db.cursor.fetchone()
        if type == 'Student':
            type = 'S'
            self.db.cursor.execute("INSERT INTO people(first_name, last_name, pather_name, group_id, type, name)"
                                   " VALUES('{}', '{}', '{}', '{}', '{}', CONCAT('{}', ' ', '{}', ' ', '{}'))".format(
                first_name,
                last_name, pather_name, number[0], type, first_name,
                last_name, pather_name))
        else:
            type = 'P'
            self.db.cursor.execute("INSERT INTO people(first_name, last_name, pather_name, type, name)"
                                   " VALUES('{}', '{}', '{}', '{}', CONCAT('{}', ' ', '{}', ' ', '{}'))".format(
                first_name,
                last_name, pather_name, type, first_name,
                last_name, pather_name))
        self.db.cursor.execute("INSERT INTO people(first_name, last_name, pather_name, group_id, type, name)"
                              " VALUES('{}', '{}', '{}', '{}', '{}', CONCAT('{}', ' ', '{}', ' ', '{}'))".format(first_name,
                                                last_name, pather_name, number[0], type, first_name,
                                                last_name, pather_name))
        self.db.cnxn.commit()
    #TODO: сделать регистрацию по номеру телефона и паролю

    def numGroupsWIthMarksClicked(self):
        name = str(self.ui.groupComboBox.currentText())
        self.db.cursor.execute("SELECT  Count(distinct SUBJECT_ID) FROM MARKS, people p, groups "
                               "WHERE P.GROUP_ID = (SELECT ID FROM GROUPS WHERE NAME = '{}')".format(name))
        number = self.db.cursor.fetchone()
        self.ui.numGroupsWIthMarksLabel.setText(str(number[0]))

    def setInitialValues(self):
        teacher_id = user_info.current_userID
        self.db.cursor.execute("SELECT name From people where user_id= '" + str(teacher_id) + "'")
        teacher_name_list = self.db.cursor.fetchone()
        self.ui.name_label.setText(str(teacher_name_list[0]))

        self.db.cursor.execute("SELECT name from groups")
        filler.fillComboBox(self.ui.groupComboBox, self.db.cursor)

        self.db.cursor.execute("SELECT name from subject")
        filler.fillComboBox(self.ui.subjectNameComboBox, self.db.cursor)

        self.db.cursor.execute("SELECT name From people where type = 'S' ")
        filler.fillComboBox(self.ui.studentNameComboBox, self.db.cursor)

        self.db.cursor.execute("SELECT name From people where type = 'P' ")
        filler.fillComboBox(self.ui.teacherNameComboBox, self.db.cursor)

        self.db.cursor.execute("SELECT name from subject")
        filler.fillComboBox(self.ui.SubjectComboBox, self.db.cursor)

        self.db.cursor.execute("SELECT G.name, round(avg(COALESCE(value, 0)), 2) FROM people p "
                               "FULL JOIN marks m on p.id = m.student_id "
                               "RIGHT JOIN GROUPS G ON G.ID = P.GROUP_ID "
                               "GROUP BY G.id;")
        filler.fillTable(self.ui.groupTableWidget, self.db.cursor, 2)

        self.db.cursor.execute("SELECT name from subject")
        filler.fillComboBox(self.ui.SubjectComboBox, self.db.cursor)

        self.set_default_marks_table()

        self.db.cursor.execute("SELECT name from groups")
        filler.fillComboBox(self.ui.groupNumComboBox, self.db.cursor)

        self.ui.typeComboBox.clear()
        self.ui.typeComboBox.addItem("Student")
        self.ui.typeComboBox.addItem("Teacher")

        self.db.cursor.execute("SELECT name from groups")
        filler.fillComboBox(self.ui.groupPointerComboBox2, self.db.cursor)

        self.db.cursor.execute("SELECT  p.name, s.name FROM MARKS M "
                               "FULL JOIN PEOPLE P ON P.ID = M.STUDENT_ID "
                               "LEFT JOIN GROUPS G ON G.ID = P.GROUP_ID "
                               "FULL Join subject s on M.subject_id = s.id")
        filler.fillTable(self.ui.studentSubjectTableWidget, self.db.cursor, 2)

        self.db.cursor.execute("select * from avgMarkByTeacher")
        filler.fillTable(self.ui.avgMarkByTeacherTableWidget, self.db.cursor, 3)

        self.db.cursor.execute("select * from avgMarkByYears")
        filler.fillTable(self.ui.yearMarksTableWidget, self.db.cursor, 2)

        self.ui.yearComboBox.clear()
        self.ui.yearComboBox.addItem("")
        for i in range (2015, datetime.date.today().year) :
            self.ui.yearComboBox.addItem(str(i))