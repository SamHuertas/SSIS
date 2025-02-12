# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ssisui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainPage(object):
    def setupUi(self, MainPage):
        if not MainPage.objectName():
            MainPage.setObjectName(u"MainPage")
        MainPage.resize(1491, 751)
        font = QFont()
        font.setPointSize(8)
        MainPage.setFont(font)
        MainPage.setStyleSheet(u"#MainPage {\n"
"	background-color: #e0f7fa;\n"
"}\n"
"\n"
"#AddStudent, #AddCollege, #AddProgram, #Database {\n"
"	background-color: #ffffff;\n"
"	border-radius: 18px;\n"
"	box-shadow: 10px 9px 7px 1px rgba(0,0,0,0.83);\n"
"}\n"
"\n"
"#MainPage QPushButton {\n"
"	background-color: #1e88e5;\n"
"	border-radius: 13px;\n"
"	box-shadow: 10px 9px 7px 1px rgba(0,0,0,0.83);\n"
"	color: white;\n"
"}\n"
"\n"
"#MainPage QPushButton:hover {\n"
"	background-color: rgb(27, 126, 212);\n"
"}\n"
"\n"
"#MainPage QPushButton:pressed {\n"
"	border: 4px solid rgb(152, 205, 229);\n"
"}\n"
"\n"
"#MainPage QLineEdit {\n"
"	border-radius: 5px;\n"
"	background-color: rgb(245, 245, 245);\n"
"	border: 1px solid rgb(235, 235, 235);\n"
"}\n"
"\n"
"#MainPage QLineEdit:hover {\n"
"	border: rgb(250, 250, 250);\n"
"}\n"
"\n"
"#MainPage QLineEdit:focus {\n"
"	border: rgb(210, 210, 210);\n"
"	background-color: rgb(231, 231, 231)\n"
"}\n"
"\n"
"QTableWidget{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(245, 245, 245);\n"
"	border: 1px sol"
                        "id rgb(235, 235, 235);\n"
"}\n"
"\n"
"#Heading {\n"
"	background-color: rgb(252, 252, 252);\n"
"}")
        self.AddStudent = QFrame(MainPage)
        self.AddStudent.setObjectName(u"AddStudent")
        self.AddStudent.setGeometry(QRect(1050, 80, 411, 271))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        self.AddStudent.setFont(font1)
        self.AddStudent.setFrameShape(QFrame.StyledPanel)
        self.AddStudent.setFrameShadow(QFrame.Raised)
        self.AddStudentText = QLabel(self.AddStudent)
        self.AddStudentText.setObjectName(u"AddStudentText")
        self.AddStudentText.setGeometry(QRect(10, 10, 151, 16))
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.AddStudentText.setFont(font2)
        self.IDText = QLabel(self.AddStudent)
        self.IDText.setObjectName(u"IDText")
        self.IDText.setGeometry(QRect(30, 40, 71, 21))
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(12)
        self.IDText.setFont(font3)
        self.FNameText = QLabel(self.AddStudent)
        self.FNameText.setObjectName(u"FNameText")
        self.FNameText.setGeometry(QRect(30, 70, 81, 21))
        self.FNameText.setFont(font3)
        self.LNameText = QLabel(self.AddStudent)
        self.LNameText.setObjectName(u"LNameText")
        self.LNameText.setGeometry(QRect(30, 100, 81, 21))
        self.LNameText.setFont(font3)
        self.YLevelText = QLabel(self.AddStudent)
        self.YLevelText.setObjectName(u"YLevelText")
        self.YLevelText.setGeometry(QRect(30, 160, 81, 21))
        self.YLevelText.setFont(font3)
        self.IDTB = QLineEdit(self.AddStudent)
        self.IDTB.setObjectName(u"IDTB")
        self.IDTB.setGeometry(QRect(150, 40, 231, 21))
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(10)
        self.IDTB.setFont(font4)
        self.IDTB.setStyleSheet(u"")
        self.GenderDD = QComboBox(self.AddStudent)
        self.GenderDD.setObjectName(u"GenderDD")
        self.GenderDD.setGeometry(QRect(150, 130, 81, 21))
        self.GenderDD.setFont(font1)
        self.GenderText = QLabel(self.AddStudent)
        self.GenderText.setObjectName(u"GenderText")
        self.GenderText.setGeometry(QRect(30, 130, 81, 21))
        self.GenderText.setFont(font3)
        self.YLevelDD = QComboBox(self.AddStudent)
        self.YLevelDD.setObjectName(u"YLevelDD")
        self.YLevelDD.setGeometry(QRect(150, 160, 81, 21))
        self.YLevelDD.setFont(font1)
        self.FNameTB = QLineEdit(self.AddStudent)
        self.FNameTB.setObjectName(u"FNameTB")
        self.FNameTB.setGeometry(QRect(150, 70, 231, 21))
        self.FNameTB.setFont(font4)
        self.LNameTB = QLineEdit(self.AddStudent)
        self.LNameTB.setObjectName(u"LNameTB")
        self.LNameTB.setGeometry(QRect(150, 100, 231, 21))
        self.LNameTB.setFont(font4)
        self.PCodeText = QLabel(self.AddStudent)
        self.PCodeText.setObjectName(u"PCodeText")
        self.PCodeText.setGeometry(QRect(30, 190, 111, 21))
        self.PCodeText.setFont(font3)
        self.PCodeDD = QComboBox(self.AddStudent)
        self.PCodeDD.setObjectName(u"PCodeDD")
        self.PCodeDD.setGeometry(QRect(150, 190, 81, 21))
        self.PCodeDD.setFont(font1)
        self.AddStudentButton = QPushButton(self.AddStudent)
        self.AddStudentButton.setObjectName(u"AddStudentButton")
        self.AddStudentButton.setGeometry(QRect(280, 230, 121, 31))
        font5 = QFont()
        font5.setFamilies([u"Roboto"])
        font5.setPointSize(14)
        self.AddStudentButton.setFont(font5)
        self.AddStudentButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.AddProgram = QFrame(MainPage)
        self.AddProgram.setObjectName(u"AddProgram")
        self.AddProgram.setGeometry(QRect(1050, 540, 411, 181))
        self.AddProgram.setFont(font1)
        self.AddProgram.setFrameShape(QFrame.StyledPanel)
        self.AddProgram.setFrameShadow(QFrame.Raised)
        self.AddProgramText = QLabel(self.AddProgram)
        self.AddProgramText.setObjectName(u"AddProgramText")
        self.AddProgramText.setGeometry(QRect(10, 10, 151, 21))
        self.AddProgramText.setFont(font2)
        self.PCodeText2 = QLabel(self.AddProgram)
        self.PCodeText2.setObjectName(u"PCodeText2")
        self.PCodeText2.setGeometry(QRect(30, 40, 111, 21))
        self.PCodeText2.setFont(font3)
        self.PCodeTB = QLineEdit(self.AddProgram)
        self.PCodeTB.setObjectName(u"PCodeTB")
        self.PCodeTB.setGeometry(QRect(150, 40, 221, 21))
        self.PCodeTB.setFont(font4)
        self.PNameText = QLabel(self.AddProgram)
        self.PNameText.setObjectName(u"PNameText")
        self.PNameText.setGeometry(QRect(30, 70, 111, 21))
        self.PNameText.setFont(font3)
        self.PCollCodeText = QLabel(self.AddProgram)
        self.PCollCodeText.setObjectName(u"PCollCodeText")
        self.PCollCodeText.setGeometry(QRect(30, 100, 111, 21))
        self.PCollCodeText.setFont(font3)
        self.PNameTB = QLineEdit(self.AddProgram)
        self.PNameTB.setObjectName(u"PNameTB")
        self.PNameTB.setGeometry(QRect(150, 70, 221, 21))
        self.PNameTB.setFont(font4)
        self.AddProgramButton = QPushButton(self.AddProgram)
        self.AddProgramButton.setObjectName(u"AddProgramButton")
        self.AddProgramButton.setGeometry(QRect(280, 140, 121, 31))
        self.AddProgramButton.setFont(font5)
        self.AddProgramButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.PCollCodeDD = QComboBox(self.AddProgram)
        self.PCollCodeDD.setObjectName(u"PCollCodeDD")
        self.PCollCodeDD.setGeometry(QRect(150, 100, 81, 21))
        self.PCollCodeDD.setFont(font1)
        self.AddCollege = QFrame(MainPage)
        self.AddCollege.setObjectName(u"AddCollege")
        self.AddCollege.setGeometry(QRect(1050, 370, 411, 151))
        self.AddCollege.setFont(font1)
        self.AddCollege.setFrameShape(QFrame.StyledPanel)
        self.AddCollege.setFrameShadow(QFrame.Raised)
        self.AddCollegeText = QLabel(self.AddCollege)
        self.AddCollegeText.setObjectName(u"AddCollegeText")
        self.AddCollegeText.setGeometry(QRect(10, 10, 151, 21))
        self.AddCollegeText.setFont(font2)
        self.CCodeText = QLabel(self.AddCollege)
        self.CCodeText.setObjectName(u"CCodeText")
        self.CCodeText.setGeometry(QRect(30, 40, 111, 21))
        self.CCodeText.setFont(font3)
        self.CCodeTB = QLineEdit(self.AddCollege)
        self.CCodeTB.setObjectName(u"CCodeTB")
        self.CCodeTB.setGeometry(QRect(150, 40, 231, 21))
        self.CCodeTB.setFont(font4)
        self.CNameText = QLabel(self.AddCollege)
        self.CNameText.setObjectName(u"CNameText")
        self.CNameText.setGeometry(QRect(30, 70, 111, 21))
        self.CNameText.setFont(font3)
        self.CNameTB = QLineEdit(self.AddCollege)
        self.CNameTB.setObjectName(u"CNameTB")
        self.CNameTB.setGeometry(QRect(150, 70, 231, 21))
        self.CNameTB.setFont(font4)
        self.AddCollegeButton = QPushButton(self.AddCollege)
        self.AddCollegeButton.setObjectName(u"AddCollegeButton")
        self.AddCollegeButton.setGeometry(QRect(280, 110, 121, 31))
        self.AddCollegeButton.setFont(font5)
        self.AddCollegeButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Database = QFrame(MainPage)
        self.Database.setObjectName(u"Database")
        self.Database.setGeometry(QRect(30, 80, 1001, 641))
        self.Database.setFont(font1)
        self.Database.setFrameShape(QFrame.StyledPanel)
        self.Database.setFrameShadow(QFrame.Raised)
        self.SearchText = QLabel(self.Database)
        self.SearchText.setObjectName(u"SearchText")
        self.SearchText.setGeometry(QRect(20, 20, 81, 21))
        self.SearchText.setFont(font3)
        self.SearchDD = QComboBox(self.Database)
        self.SearchDD.setObjectName(u"SearchDD")
        self.SearchDD.setGeometry(QRect(100, 20, 81, 22))
        self.SearchDD.setFont(font1)
        self.SearchTB = QLineEdit(self.Database)
        self.SearchTB.setObjectName(u"SearchTB")
        self.SearchTB.setGeometry(QRect(190, 20, 211, 21))
        self.SearchTB.setFont(font3)
        self.SearchButton = QPushButton(self.Database)
        self.SearchButton.setObjectName(u"SearchButton")
        self.SearchButton.setGeometry(QRect(410, 20, 61, 21))
        self.SearchButton.setFont(font3)
        self.SearchButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.SearchButton.setStyleSheet(u"#SearchButton\n"
"{	\n"
"	background-color: #1e88e5;\n"
"	border-radius: 2px;\n"
"	box-shadow: 10px 9px 7px 1px rgba(0,0,0,0.83);\n"
"	color: white;\n"
"}\n"
"#SearchButton:pressed {\n"
"	border: 3px solid rgb(152, 205, 229);\n"
"}")
        self.SortText = QLabel(self.Database)
        self.SortText.setObjectName(u"SortText")
        self.SortText.setGeometry(QRect(20, 50, 81, 21))
        self.SortText.setFont(font3)
        self.SortDD = QComboBox(self.Database)
        self.SortDD.addItem("")
        self.SortDD.addItem("")
        self.SortDD.addItem("")
        self.SortDD.addItem("")
        self.SortDD.addItem("")
        self.SortDD.setObjectName(u"SortDD")
        self.SortDD.setGeometry(QRect(100, 50, 81, 22))
        self.SortDD.setFont(font1)
        self.tableWidget = QTableWidget(self.Database)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 90, 961, 491))
        self.tableWidget.setFont(font1)
        self.EditStudentButton = QPushButton(self.Database)
        self.EditStudentButton.setObjectName(u"EditStudentButton")
        self.EditStudentButton.setEnabled(True)
        self.EditStudentButton.setGeometry(QRect(20, 590, 121, 31))
        self.EditStudentButton.setFont(font5)
        self.EditStudentButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.DeleteStudentButton = QPushButton(self.Database)
        self.DeleteStudentButton.setObjectName(u"DeleteStudentButton")
        self.DeleteStudentButton.setEnabled(True)
        self.DeleteStudentButton.setGeometry(QRect(150, 590, 141, 31))
        self.DeleteStudentButton.setFont(font5)
        self.DeleteStudentButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Heading = QFrame(MainPage)
        self.Heading.setObjectName(u"Heading")
        self.Heading.setGeometry(QRect(0, 0, 1491, 51))
        self.Heading.setFrameShape(QFrame.StyledPanel)
        self.Heading.setFrameShadow(QFrame.Raised)
        self.HeadingTitle = QLabel(self.Heading)
        self.HeadingTitle.setObjectName(u"HeadingTitle")
        self.HeadingTitle.setGeometry(QRect(40, 10, 211, 31))
        self.HeadingTitle.setFont(font3)

        self.retranslateUi(MainPage)

        QMetaObject.connectSlotsByName(MainPage)
    # setupUi

    def retranslateUi(self, MainPage):
        MainPage.setWindowTitle(QCoreApplication.translate("MainPage", u"Dialog", None))
        self.AddStudentText.setText(QCoreApplication.translate("MainPage", u"Add Student", None))
        self.IDText.setText(QCoreApplication.translate("MainPage", u"ID #", None))
        self.FNameText.setText(QCoreApplication.translate("MainPage", u"First Name", None))
        self.LNameText.setText(QCoreApplication.translate("MainPage", u"Last Name", None))
        self.YLevelText.setText(QCoreApplication.translate("MainPage", u"Year Level", None))
        self.IDTB.setPlaceholderText("")
        self.GenderText.setText(QCoreApplication.translate("MainPage", u"Gender", None))
        self.FNameTB.setPlaceholderText("")
        self.LNameTB.setPlaceholderText("")
        self.PCodeText.setText(QCoreApplication.translate("MainPage", u"Program Code", None))
        self.AddStudentButton.setText(QCoreApplication.translate("MainPage", u"Add Student", None))
        self.AddProgramText.setText(QCoreApplication.translate("MainPage", u"Add Program", None))
        self.PCodeText2.setText(QCoreApplication.translate("MainPage", u"Code", None))
        self.PCodeTB.setPlaceholderText(QCoreApplication.translate("MainPage", u"ex. BSCS", None))
        self.PNameText.setText(QCoreApplication.translate("MainPage", u"Program Name", None))
        self.PCollCodeText.setText(QCoreApplication.translate("MainPage", u"College Code", None))
        self.PNameTB.setText("")
        self.PNameTB.setPlaceholderText(QCoreApplication.translate("MainPage", u"ex. Bachelor of Science in Computer Science", None))
        self.AddProgramButton.setText(QCoreApplication.translate("MainPage", u"Add Program", None))
        self.AddCollegeText.setText(QCoreApplication.translate("MainPage", u"Add College", None))
        self.CCodeText.setText(QCoreApplication.translate("MainPage", u"Code", None))
        self.CCodeTB.setText("")
        self.CCodeTB.setPlaceholderText(QCoreApplication.translate("MainPage", u"ex. CCS", None))
        self.CNameText.setText(QCoreApplication.translate("MainPage", u"College Name", None))
        self.CNameTB.setText("")
        self.CNameTB.setPlaceholderText(QCoreApplication.translate("MainPage", u"ex. College of Computer Studies", None))
        self.AddCollegeButton.setText(QCoreApplication.translate("MainPage", u"Add College", None))
        self.SearchText.setText(QCoreApplication.translate("MainPage", u"Search by:", None))
        self.SearchTB.setPlaceholderText("")
        self.SearchButton.setText(QCoreApplication.translate("MainPage", u"Search", None))
        self.SortText.setText(QCoreApplication.translate("MainPage", u"Sort by:", None))
        self.SortDD.setItemText(0, QCoreApplication.translate("MainPage", u"ID#", None))
        self.SortDD.setItemText(1, QCoreApplication.translate("MainPage", u"First Name", None))
        self.SortDD.setItemText(2, QCoreApplication.translate("MainPage", u"Last Name", None))
        self.SortDD.setItemText(3, QCoreApplication.translate("MainPage", u"Year Level", None))
        self.SortDD.setItemText(4, QCoreApplication.translate("MainPage", u"Program Code", None))

        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainPage", u"ID#", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainPage", u"First Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainPage", u"Last Name", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainPage", u"Year Level", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainPage", u"Gender", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainPage", u"Program Code", None));
        self.EditStudentButton.setText(QCoreApplication.translate("MainPage", u"Edit Student", None))
        self.DeleteStudentButton.setText(QCoreApplication.translate("MainPage", u"Delete Student", None))
        self.HeadingTitle.setText(QCoreApplication.translate("MainPage", u"Student Information System", None))
    # retranslateUi

