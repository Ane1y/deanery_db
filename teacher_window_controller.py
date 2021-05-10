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
        self.ui.subjectNameComboBox.currentIndexChanged.connect(self.studentName_changed)

        # self.ui.add_record_Button.clicked.connect(self.add_record_Button_clicked)
        # self.ui.patients_comboBox.currentIndexChanged.connect(self.patients_change)
        # self.ui.form_queue_button.clicked.connect(self.form_queue_button_clicked)
        # self.ui.show_all_med_record_button.clicked.connect(self.show_all_med_records)
        # self.ui.change_med_record_button.clicked.connect(self.change_med_record)
        # self.ui.date_med_record_button.clicked.connect(self.show_by_date)

        self.show()
    def set_default_marks_table(self):
        self.db.cursor.execute("SELECT st.name, s.name, t.name, value, date from marks "
                               "left join people st on MARKS.STUDENT_ID = st.ID"
                               " left join people t on MARKS.TEACHER_ID = t.id "
                               "left join subject s on MARKS.SUBJECT_ID = s.id")
        filler.fillTable(self.ui.marksTableWidget, self.db.cursor, 5)

    def studentName_changed(self):
        student_name = str(self.ui.studentNameComboBox.currentText())
        teacher_name = str(self.ui.teacherNameComboBox.currentText())
        subject_name = str(self.ui.subjectNameComboBox.currentText())

        if self.ui.studentNameComboBox.currentIndex() == 0 and self.ui.teacherNameComboBox.currentIndex() == 0 and \
                self.ui.subjectNameComboBox.currentIndex() == 0:
            self.set_default_marks_table()
        elif self.ui.studentNameComboBox.currentIndex() == 0 and self.ui.subjectNameComboBox.currentIndex() == 0:
            self.db.cursor.execute("SELECT st.name, s.name, t.name, value, date from marks "
                               "left join people st on MARKS.STUDENT_ID = st.ID"
                               " left join people t on MARKS.TEACHER_ID = t.id "
                               "left join subject s on MARKS.SUBJECT_ID = s.id "
                                   "where t.name = '{}'".format(teacher_name))
            filler.fillTable(self.ui.marksTableWidget, self.db.cursor, 5)
        elif self.ui.teacherNameComboBox.currentIndex() == 0 and self.ui.subjectNameComboBox.currentIndex() == 0:

            self.db.cursor.execute("SELECT st.name, s.name, t.name, value, date from marks "
                               "left join people st on MARKS.STUDENT_ID = st.ID"
                               " left join people t on MARKS.TEACHER_ID = t.id "
                               "left join subject s on MARKS.SUBJECT_ID = s.id "
                                   "where st.name = '{}'".format(student_name))
            filler.fillTable(self.ui.marksTableWidget, self.db.cursor, 5)
        elif self.ui.subjectNameComboBox.currentIndex() == 0 and self.ui.studentNameComboBox.currentIndex() == 0 :
            self.db.cursor.execute("SELECT st.name, s.name, t.name, value, date from marks "
                               "left join people st on MARKS.STUDENT_ID = st.ID"
                               " left join people t on MARKS.TEACHER_ID = t.id "
                               "left join subject s on MARKS.SUBJECT_ID = s.id"
                                " where t.name = '{}'".format(teacher_name))
            filler.fillTable(self.ui.marksTableWidget, self.db.cursor, 5)
        elif self.ui.subjectNameComboBox.currentIndex() == 0 and self.ui.teacherNameComboBox.currentIndex() == 0:
            self.db.cursor.execute("SELECT st.name, s.name, t.name, value, date from marks "
                               "left join people st on MARKS.STUDENT_ID = st.ID"
                               " left join people t on MARKS.TEACHER_ID = t.id "
                               "left join subject s on MARKS.SUBJECT_ID = s.id"
                                " where t.name = '{}'".format(student_name))
            filler.fillTable(self.ui.marksTableWidget, self.db.cursor, 5)

        elif self.ui.subjectNameComboBox.currentIndex() == 0:
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
        #self.db.cursor.execute("INSERT INTO people(first_name, last_name, pather_name, group_id, type)"
                              # " VALUES('Смирнов', 'Антон', 'Николаевич', 6, 'S')")


    def numGroupsWIthMarksClicked(self):
        name = str(self.ui.groupComboBox.currentText())
        self.db.cursor.execute("SELECT  Count(distinct SUBJECT_ID) FROM MARKS, people p, groups "
                               "WHERE P.GROUP_ID = (SELECT ID FROM GROUPS WHERE NAME = '{}')".format(name))
        number = self.db.cursor.fetchone()
        self.ui.numGroupsWIthMarksLabel.setText(str(number[0]))
        # def show_by_date(self) :
    #     date = self.ui.date_med_record_dateEdit.date().toPyDate()
    #     self.db.cursor.execute("SELECT date, P.name, diagnosis FROM medical_records "
    #                            "LEFT JOIN Patients P on P.id = patient_id "
    #                            "WHERE physician_id = (SELECT id FROM physicians WHERE user_id = '"
    #                            + str(user_info.current_userID) + "') and date = '" + str(date) + "' ORDER BY date desc")
    #     filler.fillTable(self.ui.med_journal_tableWidget, self.db.cursor, 3)
    #
    # def change_med_record(self) :
    #     new_diagnosis = str(self.ui.new_diagnosis_textEdit.toPlainText())
    #     self.db.cursor.execute("UPDATE Medical_records "
    #                                "SET diagnosis = %s "
    #                                "WHERE (id = (SELECT id FROM Medical_records WHERE physician_id = %s "
    #                                "ORDER BY id DESC LIMIT 1))", (new_diagnosis, str(user_info.current_userID)));
    #
    #     self.db.cnxn.commit()
    #     self.show_all_med_records()
    #
    # def show_all_med_records(self) :
    #     self.db.cursor.execute("SELECT date, P.name, diagnosis FROM medical_records "
    #                            "LEFT JOIN Patients P on P.id = patient_id "
    #                            "WHERE physician_id = (SELECT id FROM physicians WHERE user_id = '"
    #                            + str(user_info.current_userID) + "') ORDER BY date desc")
    #     filler.fillTable(self.ui.med_journal_tableWidget, self.db.cursor, 3)
    #
    # def show_in_selected_date(self) :
    #     date = self.ui.date_med_record_dateEdit.date().toPyDate()
    #     self.db.cursor.execute("SELECT date, P.name, diagnosis FROM medical_records "
    #                            "LEFT JOIN Patients P on P.id = patient_id "
    #                            "WHERE physician_id = (SELECT id FROM physicians WHERE user_id = '"
    #                            + str(user_info.current_userID) + "' and date = '" + str(date) + "') ORDER BY date desc")
    #     filler.fillTable(self.ui.med_journal_tableWidget, self.db.cursor, 3)
    #
    # def patients_change(self):
    #     print("Change patient")
    #     self.ui.med_card_tableWidget.setRowCount(0)
    #     current_patient = str(self.ui.patients_comboBox.currentText())
    #
    #     sqlcmd = ("SELECT date, Ph.name, diagnosis FROM medical_records "
    #                            "LEFT JOIN Physicians Ph on Ph.id = physician_id "
    #                            "WHERE patient_id = (SELECT id FROM patients WHERE name = '"
    #                            + current_patient + "') ORDER BY date desc")
    #     self.db.cursor.execute(sqlcmd)
    #
    #     filler.fillTable(self.ui.med_card_tableWidget, self.db.cursor, 3)
    #
    #
    # def change_nummer_button_clicked(self):
    #     filler.changeNummer(self)
    #
    # def admin_menu_button_clicked(self) :
    #     self.menu = Admin_Controller()
    #     self.menu.show()
    #
    # def exit_button_clicked(self):
    #     filler.exitButton(self)
    #
    #
    # def form_queue_button_clicked(self):
    #     days = str(self.ui.queue_days_box.value())
    #
    #     self.db.cursor.execute("SELECT P.name, Q.time FROM Queue Q LEFT JOIN Patients P on P.id = Q.patient_id "
    #                            "WHERE ((physician_id = %s)  AND (time > current_timestamp) AND (time < current_timestamp + interval %s day))",
    #                            (user_info.current_userID, days))
    #
    #     filler.fillTable(self.ui.Queue_tableWidget, self.db.cursor, 2)
    #
    #
    # def add_record_Button_clicked(self):
    #     diagnosis = str(self.ui.diagnosis_textBrowser.toPlainText())
    #     if not(diagnosis.isalnum()) and len(diagnosis) < 3 :
    #         error_     message = QtWidgets.QErrorMessage(self)
    #         error_message.setWindowTitle("Некорректный ввод")
    #         error_message.showMessage('Подозрительный диагноз')
    #     else :
    #         name = str(self.ui.patients_comboBox.currentText())
    #         service = str(self.ui.service_comboBox.currentText())
    #         try:
    #             self.db.cursor.execute("INSERT INTO medical_records(patient_id, physician_id, date, diagnosis, service_id)" \
    #                     "VALUES ((SELECT id FROM patients WHERE name = %s), %s, %s, %s, "
    #                     "(SELECT id FROM Services WHERE name = %s))",
    #                     (name, user_info.current_userID, datetime.datetime.today().strftime('%Y-%m-%d'), diagnosis, service))
    #
    #             self.db.cnxn.commit()
    #             self.patients_change()
    #             print("smth happened")
    #         except (Exception, psycopg2.Error) as error:
    #             print("Error while connecting to PostgreSQL", error)
    #
    #


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


        # self.db.cursor.execute(
        #     "SELECT S.name, S.id from Physicians Ph LEFT JOIN Specialization S on Ph.specialization_id = S.id WHERE Ph.user_id=" + str(
        #         teacher_id))
        # spec_name = self.db.cursor.fetchone()
        # self.ui.spezialization_label.setText(spec_name[0])
        #
        # self.db.cursor.execute("SELECT passport from Physicians where user_id=" + str(teacher_id))
        # pas_name = self.db.cursor.fetchone()
        # self.ui.passport_label.setText(str(pas_name[0]))
        #
        # self.db.cursor.execute("SELECT date_of_birth from Physicians where user_id=" + str(teacher_id))
        # date_of_birth = self.db.cursor.fetchone()
        # self.ui.date_of_birth_label.setText(str(date_of_birth[0]))
        #
        # self.db.cursor.execute("SELECT phone from  authentication_data  WHERE id= %s", str(user_info.current_userID))
        # phone = self.db.cursor.fetchone()
        # self.ui.phone_number_box.setText(str(phone[0]))

        # self.db.cursor.execute("SELECT name from Services where specialization_id = %s" , str(spec_name[1]))
        # filler.fillComboBox(self.ui.service_comboBox, self.db.cursor)
        #
        # self.form_queue_button_clicked()
        # self.show_all_med_records()

