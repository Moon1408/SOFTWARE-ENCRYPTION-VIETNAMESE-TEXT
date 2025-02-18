import sys
sys.path.append("D:/HUFLIT/Nam3/BMHTTT/DoAN/Control")
from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox #[1]????????????
from ThietKe.ThietKeGiaiMaCeasar import Ui_Form  #?????????????????
from mahoaceasar_class import CCeasar #???????????
from PyQt6.QtCore import pyqtSignal

#========================================================================================
class MyGMCeasar(QWidget, Ui_Form):#[2]???????????????????????
    closeTabSignal = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Thêm xử lý sự kiện và tuỳ chỉnh giao diện người dùng tại đây
        self.textk = '' #khai báo toàn cục của lớp THIS => datamember
        self.btnGiaiMa.clicked.connect(self.GiaiMa) #????????????????????????
        self.btnOpenFile.clicked.connect(self.MoFile)
        self.btnSaveFile.clicked.connect(self.GhiFile)
        self.btnClose.clicked.connect(self.emit_close_tab_signal)
    def emit_close_tab_signal(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setWindowTitle("Xác nhận thoát")
        msg.setText("Bạn có chắc muốn thoát ứng dụng?")
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg.setStyleSheet("QMessageBox { background-color: white; }")
        ret = msg.exec()
        if ret == QMessageBox.StandardButton.Yes:
            self.closeTabSignal.emit()
        else:
            pass
    def GiaiMa(self):
        if not self.textk:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Question)
            msg.setWindowTitle("Thông báo")
            msg.setText("Bạn chưa nhập key!!!!")
            msg.setStyleSheet("QMessageBox { background-color: white; }")
            ret = msg.exec()
            self.txtKey.setFocus()
        else:
            textci = self.txtCiphertext.toPlainText() #lấy dữ liệu trong text plaintext của ThietKeMaHoaCeasar
            if not textci:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Icon.Question)
                msg.setWindowTitle("Thông báo")
                msg.setText("Bạn chưa mở file dữ liệu!!!!")
                msg.setStyleSheet("QMessageBox { background-color: white; }")
                ret = msg.exec()
                self.btnOpenFile.setFocus()
            else:
                cCeasar= CCeasar("",int(self.textk),textci) #khai báo đối tượng của lớp CCeasar
                s = cCeasar.GiaiMa() #gọi hàm mã hoá của đối tượng này
                self.txtVanBanGoc.setPlainText(s) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaCeasar
    def MoFile(self):
        # Mở file đã mã hoá riêng
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                s=''
                line = file.readline()
                while line:
                    s+=line
                    line = file.readline()
                self.txtCiphertext.setPlainText(s)
        # Mở file KEY riêng
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File KEY", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                self.textk = file.read()
                self.txtKey.setPlainText(self.textk)
                
    def GhiFile(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtVanBanGoc.toPlainText())
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Question)
            msg.setWindowTitle("Thông báo")
            msg.setText("Lưu file văn bản gốc thành công!!!!")
            msg.setStyleSheet("QMessageBox { background-color: white; }")
            ret = msg.exec()
#========================================================================================
def main():
    app = QApplication(sys.argv)
    mainMyForm = MyGMCeasar()
    mainMyForm.show()
    sys.exit(app.exec())
#========================================================================================
if __name__ == "__main__":
    main()
