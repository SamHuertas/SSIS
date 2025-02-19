from pathlib import Path
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QDialog, QLabel, QPushButton
from DuplicateStudentP import DuplicateStudentPopup
from InputError import InputErrorPopup
import csv

class Ui_EditStudentPopup(object):
    def setupUi(self, EditStudentPopup):
        EditStudentPopup.setObjectName("EditStudentPopup")
        EditStudentPopup.setFixedSize(381, 302)
        EditStudentPopup.setStyleSheet(Path('EditPopup.qss').read_text())

        # Main Frame
        self.EditStudent = QtWidgets.QFrame(parent=EditStudentPopup)
        self.EditStudent.setGeometry(QtCore.QRect(10, 10, 361, 281))
        self.EditStudent.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.EditStudent.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)

        # Labels
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)

        self.EditStudentText = QLabel("Edit Student", parent=self.EditStudent)
        self.EditStudentText.setGeometry(QtCore.QRect(10, 10, 151, 16))
        self.EditStudentText.setFont(font)
        self.EditStudentText.setObjectName("EditStudentText")

        font_normal = QtGui.QFont()
        font_normal.setFamily("Roboto")
        font_normal.setPointSize(12)

        self.IDText = QLabel("ID #", parent=self.EditStudent)
        self.IDText.setGeometry(QtCore.QRect(30, 40, 71, 21))
        self.IDText.setFont(font_normal)

        self.FNameText = QLabel("First Name", parent=self.EditStudent)
        self.FNameText.setGeometry(QtCore.QRect(30, 70, 81, 21))
        self.FNameText.setFont(font_normal)

        self.LNameText = QLabel("Last Name", parent=self.EditStudent)
        self.LNameText.setGeometry(QtCore.QRect(30, 100, 81, 21))
        self.LNameText.setFont(font_normal)

        self.GenderText = QLabel("Gender", parent=self.EditStudent)
        self.GenderText.setGeometry(QtCore.QRect(30, 130, 81, 21))
        self.GenderText.setFont(font_normal)

        self.YLevelText = QLabel("Year Level", parent=self.EditStudent)
        self.YLevelText.setGeometry(QtCore.QRect(30, 160, 81, 21))
        self.YLevelText.setFont(font_normal)

        self.PCodeText = QLabel("Program Code", parent=self.EditStudent)
        self.PCodeText.setGeometry(QtCore.QRect(30, 190, 111, 21))
        self.PCodeText.setFont(font_normal)

        # Input Fields
        font_input = QtGui.QFont("Roboto", 10)
        self.IDTB = QtWidgets.QLineEdit(parent=self.EditStudent)
        self.IDTB.setGeometry(QtCore.QRect(150, 40, 191, 21))
        self.IDTB.setFont(font_input)

        self.FNameTB = QtWidgets.QLineEdit(parent=self.EditStudent)
        self.FNameTB.setGeometry(QtCore.QRect(150, 70, 191, 21))
        self.FNameTB.setFont(font_input)

        self.LNameTB = QtWidgets.QLineEdit(parent=self.EditStudent)
        self.LNameTB.setGeometry(QtCore.QRect(150, 100, 191, 21))
        self.LNameTB.setFont(font_input)

        # Drop-down Fields
        font_dropdown = QtGui.QFont("Roboto")
        self.GenderDD = QtWidgets.QComboBox(parent=self.EditStudent)
        self.GenderDD.setGeometry(QtCore.QRect(150, 130, 81, 21))
        self.GenderDD.setFont(font_dropdown)
        self.GenderDD.addItems(["Male", "Female"])

        self.YLevelDD = QtWidgets.QComboBox(parent=self.EditStudent)
        self.YLevelDD.setGeometry(QtCore.QRect(150, 160, 81, 21))
        self.YLevelDD.setFont(font_dropdown)
        self.YLevelDD.addItems(["1", "2", "3", "4"])

        self.PCodeDD = QtWidgets.QComboBox(parent=self.EditStudent)
        self.PCodeDD.setGeometry(QtCore.QRect(150, 190, 81, 21))
        self.PCodeDD.setFont(font_dropdown)

        # Update Button
        font_button = QtGui.QFont("Roboto", 14)
        self.UpdateStudentButton = QPushButton("Update Student", parent=self.EditStudent)
        self.UpdateStudentButton.setGeometry(QtCore.QRect(10, 230, 341, 41))
        self.UpdateStudentButton.setFont(font_button)
        self.UpdateStudentButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

        self.retranslateUi(EditStudentPopup)
        QtCore.QMetaObject.connectSlotsByName(EditStudentPopup)

    def retranslateUi(self, EditStudentPopup):
        _translate = QtCore.QCoreApplication.translate
        EditStudentPopup.setWindowTitle(_translate("EditStudentPopup", "Edit Student"))

# Main Window Class
class EditStudentPopup(QDialog):
    def __init__(self, main_window, selected_row):
        super().__init__()
        self.ui = Ui_EditStudentPopup()
        self.ui.setupUi(self)
        self.setWindowTitle("Edit Student")
        self.setWindowIcon(QIcon('./StudentIcon.png'))
        self.main_window = main_window  
        self.selected_row = selected_row
        self.ui.UpdateStudentButton.clicked.connect(self.updateStudent)

    def updateStudent(self):
        new_id = self.ui.IDTB.text().strip()
        new_fname = self.ui.FNameTB.text().strip().title()
        new_lname = self.ui.LNameTB.text().strip().title()
        new_gender = self.ui.GenderDD.currentText()
        new_year_level = self.ui.YLevelDD.currentText()
        new_program_code = self.ui.PCodeDD.currentText()

        if not new_id or not new_fname or not new_lname:
            input_error = InputErrorPopup()
            input_error.setModal(True)
            input_error.exec()
            return


        for row in range(self.main_window.ui.StudentTable.rowCount()):
            existing_id = self.main_window.ui.StudentTable.item(row, 0).text()
            if new_id == existing_id and row != self.selected_row:
                self.duplicate_popup = DuplicateStudentPopup()
                self.duplicate_popup.setModal(True)
                self.duplicate_popup.show()
                return

        self.main_window.ui.StudentTable.item(self.selected_row, 0).setText(new_id)
        self.main_window.ui.StudentTable.item(self.selected_row, 1).setText(new_fname)
        self.main_window.ui.StudentTable.item(self.selected_row, 2).setText(new_lname)
        self.main_window.ui.StudentTable.item(self.selected_row, 3).setText(new_year_level)
        self.main_window.ui.StudentTable.item(self.selected_row, 4).setText(new_gender)

        program_item = self.main_window.ui.StudentTable.item(self.selected_row, 5).setText(new_program_code)
        program_item = QtWidgets.QTableWidgetItem()  
        self.main_window.ui.StudentTable.setItem(self.selected_row, 5, program_item)

        program_item.setText(new_program_code)

        if new_program_code.strip().upper() == "NULL":
            program_item.setForeground(QtGui.QColor("red")) 
        else:
            program_item.setForeground(QtGui.QColor("black"))

        self.saveUpdatedStudentToCSV()

        self.close()

    def saveUpdatedStudentToCSV(self):
        rows = []
        with open("Student.csv", "r") as file:
            reader = csv.reader(file)
            rows = list(reader)

        rows[self.selected_row + 1] = [
            self.ui.IDTB.text(),
            self.ui.FNameTB.text().title(),
            self.ui.LNameTB.text().title(),
            self.ui.YLevelDD.currentText(),
            self.ui.GenderDD.currentText(),
            self.ui.PCodeDD.currentText()
        ]

        with open("Student.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)