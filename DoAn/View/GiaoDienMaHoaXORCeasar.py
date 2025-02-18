import sys
sys.path.append("D:/HUFLIT/Nam3/BMHTTT/DoAN/Control")
from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox #[1]????????????
from ThietKe.ThietKeMaHoaXORCeasar import Ui_Form  
from mahoaXorCeasar_class import CXORCeasar #???????????
from PyQt6.QtCore import pyqtSignal
#========================================================================================
class MyMHXORCeasar(QWidget, Ui_Form):#[2]???????????????????????
    closeTabSignal = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Thêm xử lý sự kiện và tuỳ chỉnh giao diện người dùng tại đây
        self.textk = '' #khai báo toàn cục của lớp THIS => datamember
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
        self.textk = self.txtKey.toPlainText() #lấy dữ liệu trong text key của ThietKeMaHoaCeasar
        if not self.textk:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Question)
            msg.setWindowTitle("Thông báo")
            msg.setText("Bạn chưa nhập key!!!!")
            msg.setStyleSheet("QMessageBox { background-color: white; }")
            ret = msg.exec()
            self.txtKey.setFocus()
        else:
            textpl = self.txtPlaintext.toPlainText() #lấy dữ liệu trong text plaintext của ThietKeMaHoaCeasar
            if not textpl:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Icon.Question)
                msg.setWindowTitle("Thông báo")
                msg.setText("Bạn chưa mở file dữ liệu!!!!")
                msg.setStyleSheet("QMessageBox { background-color: white; }")
                ret = msg.exec()
                self.btnOpenFile.setFocus()
            else:
                cXORCeasar= CXORCeasar() #khai báo đối tượng của lớp CCeasar
                c = cXORCeasar.MaHoa(textpl,int(self.textk)) #gọi hàm mã hoá của đối tượng này
                self.txtCiphertext.setPlainText(c) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaCeasar
    def MoFile(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.txtPlaintext.setPlainText(fileContent)
    def GhiFile(self):
        # Lưu file dữ liệu đã mã hoá ciphertext
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File Mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtCiphertext.toPlainText())
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Question)
            msg.setWindowTitle("Thông báo")
            msg.setText("Lưu file mã hoá thành công!!!!")
            msg.setStyleSheet("QMessageBox { background-color: white; }")
            ret = msg.exec()

        # Lưu file KEY
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File KEY", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtKey.toPlainText())
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Question)
            msg.setWindowTitle("Thông báo")
            msg.setText("Lưu file KEY thành công!!!!")
            msg.setStyleSheet("QMessageBox { background-color: white; }")
            ret = msg.exec()
#========================================================================================
def main():
    app = QApplication(sys.argv)
    mainMyForm = MyMHXORCeasar()
    mainMyForm.show()
    sys.exit(app.exec())
#========================================================================================
if __name__ == "__main__":
    main()
