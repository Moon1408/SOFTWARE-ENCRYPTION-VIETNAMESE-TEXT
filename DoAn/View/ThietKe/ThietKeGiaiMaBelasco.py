# Form implementation generated from reading ui file 'D:\HUFLIT\Nam3\BMHTTT\DoAn\View\ThietKe\ThietKeGiaiMaBelasco.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(831, 581)
        Form.setStyleSheet("#Form{\n"
"background-color: #292C35;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"#btnGiaiMa{\n"
"    background-color: #1074CA;\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"#btnOpenFile{\n"
"    background-color: #1074CA;\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"#btnSaveFile{\n"
"    background-color: #1074CA;\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"\n"
"}\n"
"#btnClose{\n"
"    background-color: #1074CA;\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"\n"
"}")
        self.txtVanBanGoc = QtWidgets.QTextEdit(parent=Form)
        self.txtVanBanGoc.setGeometry(QtCore.QRect(80, 350, 650, 130))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.txtVanBanGoc.setFont(font)
        self.txtVanBanGoc.setStyleSheet("font: 12pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);")
        self.txtVanBanGoc.setObjectName("txtVanBanGoc")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(80, 60, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(300, 0, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.btnOpenFile = QtWidgets.QPushButton(parent=Form)
        self.btnOpenFile.setGeometry(QtCore.QRect(470, 240, 100, 38))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.btnOpenFile.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\HUFLIT\\Nam3\\BMHTTT\\DoAn\\View\\ThietKe\\../icon/mo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnOpenFile.setIcon(icon)
        self.btnOpenFile.setObjectName("btnOpenFile")
        self.txtCiphertext = QtWidgets.QTextEdit(parent=Form)
        self.txtCiphertext.setGeometry(QtCore.QRect(80, 90, 650, 130))
        self.txtCiphertext.setStyleSheet("font: 12pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);")
        self.txtCiphertext.setObjectName("txtCiphertext")
        self.btnSaveFile = QtWidgets.QPushButton(parent=Form)
        self.btnSaveFile.setGeometry(QtCore.QRect(470, 500, 100, 38))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.btnSaveFile.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:\\HUFLIT\\Nam3\\BMHTTT\\DoAn\\View\\ThietKe\\../icon/luufile.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnSaveFile.setIcon(icon1)
        self.btnSaveFile.setIconSize(QtCore.QSize(16, 16))
        self.btnSaveFile.setCheckable(False)
        self.btnSaveFile.setObjectName("btnSaveFile")
        self.btnGiaiMa = QtWidgets.QPushButton(parent=Form)
        self.btnGiaiMa.setGeometry(QtCore.QRect(630, 240, 100, 38))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.btnGiaiMa.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("D:\\HUFLIT\\Nam3\\BMHTTT\\DoAn\\View\\ThietKe\\../icon/gm_.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnGiaiMa.setIcon(icon2)
        self.btnGiaiMa.setObjectName("btnGiaiMa")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(80, 320, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.btnClose = QtWidgets.QPushButton(parent=Form)
        self.btnClose.setGeometry(QtCore.QRect(630, 500, 100, 38))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.btnClose.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("D:\\HUFLIT\\Nam3\\BMHTTT\\DoAn\\View\\ThietKe\\../icon/thoat.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnClose.setIcon(icon3)
        self.btnClose.setIconSize(QtCore.QSize(20, 20))
        self.btnClose.setCheckable(False)
        self.btnClose.setObjectName("btnClose")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(80, 250, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.txtKey = QtWidgets.QTextEdit(parent=Form)
        self.txtKey.setGeometry(QtCore.QRect(140, 250, 100, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.txtKey.setFont(font)
        self.txtKey.setStyleSheet("font: 12pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);")
        self.txtKey.setObjectName("txtKey")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Nhập nội dung đã mã hóa:"))
        self.label.setText(_translate("Form", "Giải mã BELASCO"))
        self.btnOpenFile.setText(_translate("Form", "Mở file"))
        self.btnSaveFile.setText(_translate("Form", "Lưu file"))
        self.btnGiaiMa.setText(_translate("Form", "Giải mã"))
        self.label_4.setText(_translate("Form", "Nội dung đã mã hoá:"))
        self.btnClose.setText(_translate("Form", "Thoát"))
        self.label_3.setText(_translate("Form", "Key :"))
