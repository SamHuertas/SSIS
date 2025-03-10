from pathlib import Path
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QDialog, QLabel, QPushButton

class Ui_DeleteProgramPopup(object):
    def setupUi(self, DeleteProgramPopup):
        DeleteProgramPopup.setObjectName("DeleteProgramPopup")
        DeleteProgramPopup.setFixedSize(371, 201)
        DeleteProgramPopup.setStyleSheet(Path('Styles/DeletePopup.qss').read_text())

        # Confirmation Label
        self.Confirmation = QLabel(DeleteProgramPopup)
        self.Confirmation.setObjectName("Confirmation")
        self.Confirmation.setGeometry(QtCore.QRect(100, 20, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Confirmation.setFont(font)
        self.Confirmation.setAutoFillBackground(False)
        self.Confirmation.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.Confirmation.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Confirmation.setWordWrap(True)

        # Confirmation_2 Label
        self.Confirmation_2 = QLabel(DeleteProgramPopup)
        self.Confirmation_2.setObjectName("Confirmation_2")
        self.Confirmation_2.setGeometry(QtCore.QRect(30, 70, 311, 51))
        font1 = QtGui.QFont()
        font1.setFamily("Roboto")
        font1.setPointSize(11)
        self.Confirmation_2.setFont(font1)
        self.Confirmation_2.setAutoFillBackground(False)
        self.Confirmation_2.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.Confirmation_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Confirmation_2.setWordWrap(True)

        # Cancel Button
        self.CancelButton = QPushButton(DeleteProgramPopup)
        self.CancelButton.setObjectName("CancelButton")
        self.CancelButton.setGeometry(QtCore.QRect(60, 130, 121, 41))
        font2 = QtGui.QFont()
        font2.setFamily("Roboto")
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setWeight(50)
        self.CancelButton.setFont(font2)

        # Delete Button
        self.DeleteButton = QPushButton(DeleteProgramPopup)
        self.DeleteButton.setObjectName("DeleteButton")
        self.DeleteButton.setGeometry(QtCore.QRect(190, 130, 121, 41))
        self.DeleteButton.setFont(font2)

        self.retranslateUi(DeleteProgramPopup)
        QtCore.QMetaObject.connectSlotsByName(DeleteProgramPopup)

    def retranslateUi(self, DeleteProgramPopup):
        _translate = QtCore.QCoreApplication.translate
        DeleteProgramPopup.setWindowTitle(_translate("DeleteProgramPopup", "Dialog"))
        self.Confirmation.setText(_translate("DeleteProgramPopup", "Are you sure?"))
        self.Confirmation_2.setText(_translate("DeleteProgramPopup", "You are about to delete a program from the database"))
        self.CancelButton.setText(_translate("DeleteProgramPopup", "Cancel"))
        self.DeleteButton.setText(_translate("DeleteProgramPopup", "Delete"))

class DeleteProgramPopup(QDialog):
    def __init__(self, program_code, parent=None):
        super().__init__(parent)
        self.ui = Ui_DeleteProgramPopup()
        self.ui.setupUi(self)
        self.setWindowTitle('Confirm Delete')
        self.setWindowIcon(QIcon('Assets/StudentIcon.png'))

        self.program_code = program_code

        self.ui.CancelButton.clicked.connect(self.close)
        self.ui.DeleteButton.clicked.connect(self.delete_program)

    def delete_program(self, program_code):
        with open("Database/Program.csv", "r") as file:
            lines = file.readlines()

        with open("Database/Program.csv", "w") as file:
            for line in lines:
                if not line.startswith(self.program_code + ","):
                    file.write(line)

        student_lines = []
        with open("Database/Student.csv", "r") as file:
                student_lines = file.readlines()
        
        with open("Database/Student.csv", "w") as file:
            for line in student_lines:
                data = line.strip().split(",")
                if data[5] == self.program_code:  
                    data[5] = "NULL"  
                file.write(",".join(data) + "\n")
        
        self.parent().openStudentCSV() 
        self.parent().openProgramCSV() 
        self.parent().ui.ProgramTable.clearSelection()
        self.close()
