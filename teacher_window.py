# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/teacher_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(972, 850)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(30, 10, 911, 791))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.name_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.name_label.setObjectName("name_label")
        self.horizontalLayout.addWidget(self.name_label)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.mainTabWidget = QtWidgets.QTabWidget(self.verticalLayoutWidget_4)
        self.mainTabWidget.setObjectName("mainTabWidget")
        self.groupsTab = QtWidgets.QWidget()
        self.groupsTab.setObjectName("groupsTab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupsTab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 871, 711))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.groupComboBox.setObjectName("groupComboBox")
        self.horizontalLayout_2.addWidget(self.groupComboBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.groupTableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.groupTableWidget.setObjectName("groupTableWidget")
        self.groupTableWidget.setColumnCount(2)
        self.groupTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.groupTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.groupTableWidget.setHorizontalHeaderItem(1, item)
        self.verticalLayout.addWidget(self.groupTableWidget)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_9.addWidget(self.label_4)
        self.firstNameLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.firstNameLineEdit.setObjectName("firstNameLineEdit")
        self.horizontalLayout_9.addWidget(self.firstNameLineEdit)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_9.addWidget(self.label_5)
        self.lastNameLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lastNameLineEdit.setObjectName("lastNameLineEdit")
        self.horizontalLayout_9.addWidget(self.lastNameLineEdit)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_9.addWidget(self.label_6)
        self.patherNameLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.patherNameLineEdit.setObjectName("patherNameLineEdit")
        self.horizontalLayout_9.addWidget(self.patherNameLineEdit)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.typeComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.typeComboBox.setObjectName("typeComboBox")
        self.horizontalLayout_9.addWidget(self.typeComboBox)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_9.addWidget(self.label_8)
        self.groupNumComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.groupNumComboBox.setObjectName("groupNumComboBox")
        self.horizontalLayout_9.addWidget(self.groupNumComboBox)
        self.addUserPushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.addUserPushButton.setObjectName("addUserPushButton")
        self.horizontalLayout_9.addWidget(self.addUserPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_8.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_8.addWidget(self.pushButton_4)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.numGroupsWIthMarksButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numGroupsWIthMarksButton.sizePolicy().hasHeightForWidth())
        self.numGroupsWIthMarksButton.setSizePolicy(sizePolicy)
        self.numGroupsWIthMarksButton.setObjectName("numGroupsWIthMarksButton")
        self.horizontalLayout_3.addWidget(self.numGroupsWIthMarksButton)
        self.numGroupsWIthMarksLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.numGroupsWIthMarksLabel.setText("")
        self.numGroupsWIthMarksLabel.setObjectName("numGroupsWIthMarksLabel")
        self.horizontalLayout_3.addWidget(self.numGroupsWIthMarksLabel)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.mainTabWidget.addTab(self.groupsTab, "")
        self.marksTab = QtWidgets.QWidget()
        self.marksTab.setObjectName("marksTab")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.marksTab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 10, 871, 711))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.studentNameComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.studentNameComboBox.setObjectName("studentNameComboBox")
        self.horizontalLayout_4.addWidget(self.studentNameComboBox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.teacherNameComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.teacherNameComboBox.setObjectName("teacherNameComboBox")
        self.horizontalLayout_4.addWidget(self.teacherNameComboBox)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.SubjectComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.SubjectComboBox.setObjectName("SubjectComboBox")
        self.horizontalLayout_4.addWidget(self.SubjectComboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem4)
        self.markSpinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.markSpinBox.setMinimum(2)
        self.markSpinBox.setMaximum(5)
        self.markSpinBox.setObjectName("markSpinBox")
        self.horizontalLayout_10.addWidget(self.markSpinBox)
        self.addMarkPushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.addMarkPushButton.setObjectName("addMarkPushButton")
        self.horizontalLayout_10.addWidget(self.addMarkPushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.marksTableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget_2)
        self.marksTableWidget.setObjectName("marksTableWidget")
        self.marksTableWidget.setColumnCount(5)
        self.marksTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.marksTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.marksTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.marksTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.marksTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.marksTableWidget.setHorizontalHeaderItem(4, item)
        self.verticalLayout_2.addWidget(self.marksTableWidget)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_5.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_5.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_5.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_5.addWidget(self.pushButton_8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.mainTabWidget.addTab(self.marksTab, "")
        self.subjectsTab = QtWidgets.QWidget()
        self.subjectsTab.setObjectName("subjectsTab")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.subjectsTab)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 10, 871, 711))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.subjectNameComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.subjectNameComboBox.setObjectName("subjectNameComboBox")
        self.horizontalLayout_6.addWidget(self.subjectNameComboBox)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.subjectTableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget_3)
        self.subjectTableWidget.setObjectName("subjectTableWidget")
        self.subjectTableWidget.setColumnCount(0)
        self.subjectTableWidget.setRowCount(0)
        self.verticalLayout_3.addWidget(self.subjectTableWidget)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_9 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_7.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_7.addWidget(self.pushButton_10)
        self.pushButton_11 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_7.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_7.addWidget(self.pushButton_12)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.mainTabWidget.addTab(self.subjectsTab, "")
        self.verticalLayout_4.addWidget(self.mainTabWidget)

        self.retranslateUi(Dialog)
        self.mainTabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.name_label.setText(_translate("Dialog", "TextLabel"))
        item = self.groupTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Номер группы"))
        item = self.groupTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Средний балл"))
        self.label_4.setText(_translate("Dialog", "Фамилия"))
        self.label_5.setText(_translate("Dialog", "Имя"))
        self.label_6.setText(_translate("Dialog", "Отчество"))
        self.label_7.setText(_translate("Dialog", "Роль"))
        self.label_8.setText(_translate("Dialog", "Номер группы"))
        self.addUserPushButton.setText(_translate("Dialog", "Добавить пользователя"))
        self.pushButton_3.setText(_translate("Dialog", "PushButton"))
        self.pushButton_4.setText(_translate("Dialog", "PushButton"))
        self.numGroupsWIthMarksButton.setText(_translate("Dialog", "Число предметов, по которым есть оценки у группы"))
        self.pushButton_2.setText(_translate("Dialog", "PushButton"))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.groupsTab), _translate("Dialog", "Groups"))
        self.label.setText(_translate("Dialog", "Студент:"))
        self.label_2.setText(_translate("Dialog", "Преподаватель:"))
        self.label_3.setText(_translate("Dialog", "Предмет"))
        self.addMarkPushButton.setText(_translate("Dialog", "Добавить оценку"))
        item = self.marksTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Студент"))
        item = self.marksTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Предмет"))
        item = self.marksTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Учитель"))
        item = self.marksTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Оценка"))
        item = self.marksTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Дата"))
        self.pushButton_5.setText(_translate("Dialog", "PushButton"))
        self.pushButton_6.setText(_translate("Dialog", "PushButton"))
        self.pushButton_7.setText(_translate("Dialog", "PushButton"))
        self.pushButton_8.setText(_translate("Dialog", "PushButton"))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.marksTab), _translate("Dialog", "Marks"))
        self.pushButton_9.setText(_translate("Dialog", "PushButton"))
        self.pushButton_10.setText(_translate("Dialog", "PushButton"))
        self.pushButton_11.setText(_translate("Dialog", "PushButton"))
        self.pushButton_12.setText(_translate("Dialog", "PushButton"))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.subjectsTab), _translate("Dialog", "Subjects"))
