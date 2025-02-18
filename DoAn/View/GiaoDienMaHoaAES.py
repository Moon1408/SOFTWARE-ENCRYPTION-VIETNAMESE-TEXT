import sys
sys.path.append("D:/HUFLIT/Nam3/BMHTTT/DoAN/Control")
from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox #[1]????????????
from ThietKe.ThietKeMaHoaAES import Ui_Form
from mahoaAES_class import CAES
from PyQt6.QtCore import pyqtSignal


class MyMHAES(QWidget, Ui_Form):
    closeTabSignal = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)     
    # Thêm xử lý sự kiện và tuỳ chỉnh giao diện người dùng tại đây
        self.textk = '' #khai báo toàn cục của lớp THIS => datamember
        self.c = ''
        self.p = ''
        self.btnMaHoa.clicked.connect(self.MaHoa)
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
    def MaHoa(self):
        textpl = self.txtPlaintext.toPlainText() #lấy dữ liệu trong text plaintext của ThietKeMaHoaVignere
        if not textpl:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Question)
            msg.setWindowTitle("Thông báo")
            msg.setText("Bạn chưa mở file dữ liệu!!!!")
            msg.setStyleSheet("QMessageBox { background-color: white; }")
            ret = msg.exec()
            self.btnOpenFile.setFocus()
        else:
            cAES = CAES()
            self.c, self.textk = cAES.MaHoa(self.p) #gọi hàm mã hoá của đối tượng này
            #print(self.c)
            self.txtCiphertext.setPlainText(self.c.decode('utf-8')) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaVignere
    def MoFile(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                self.p = file.read()
                self.txtPlaintext.setPlainText(self.p)
    def GhiFile(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'wb') as file:
                file.write(self.c)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Question)
            msg.setWindowTitle("Thông báo")
            msg.setText("Lưu file mã hoá thành công!!!!")
            msg.setStyleSheet("QMessageBox { background-color: white; }")
            ret = msg.exec()
            
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File KEY", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'wb') as file:
                file.write(self.textk)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Question)
            msg.setWindowTitle("Thông báo")
            msg.setText("Lưu file KEY thành công!!!!")
            msg.setStyleSheet("QMessageBox { background-color: white; }")
            ret = msg.exec()
#========================================================================================
def main():
    app = QApplication(sys.argv)
    mainMyForm = MyMHAES()
    mainMyForm.show()
    sys.exit(app.exec())
#========================================================================================
if __name__ == "__main__":
    main()
