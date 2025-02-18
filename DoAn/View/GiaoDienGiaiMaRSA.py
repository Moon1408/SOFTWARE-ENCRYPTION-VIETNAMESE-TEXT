import sys
sys.path.append("D:/HUFLIT/Nam3/BMHTTT/DoAN/Control")
from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox #[1]????????????
from ThietKe.ThietKeGiaiMaRSA  import Ui_Form  
import mahoaRSA  #???????????
from PyQt6.QtCore import pyqtSignal

#========================================================================================
class MyGMRSA(QWidget, Ui_Form):#[2]???????????????????????
    closeTabSignal = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
       # Thêm xử lý sự kiện và tuỳ chỉnh giao diện người dùng tại đây
        self.s = '' #khai báo toàn cục của lớp THIS => datamember
        self.btnGiaiMa.clicked.connect(self.GiaiMa)
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
        textci = self.txtCiphertext.toPlainText() #lấy dữ liệu trong text ciphertext của ThietKeMaHoaVignere
        if not textci:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Question)
            msg.setWindowTitle("Thông báo")
            msg.setText("Bạn chưa mở file dữ liệu!!!!")
            msg.setStyleSheet("QMessageBox { background-color: white; }")
            ret = msg.exec()
            self.btnOpenFile.setFocus()
        else:
            n=4255903; d=2480777
            ci=[]
            arr_S = self.s.split(" ")
            for i in arr_S:
                ci.append(int(i))
            c = mahoaRSA.GiaiMa(ci,d,n) #gọi hàm mã hoá của đối tượng này
            s = ''
            for i in c:
                s+= str(i)
            self.txtVanBanGoc.setPlainText(s) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaVignere
    def MoFile(self):
        #Mở file dữ liệu đã mã hoá
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r') as file:
                self.s = file.read()
                self.s =self.s.rstrip()
                self.txtCiphertext.setPlainText(self.s)

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
#=========================================================================================
def main():
    app = QApplication(sys.argv)
    mainMyForm = MyGMRSA()
    mainMyForm.show()
    sys.exit(app.exec())
#========================================================================================
if __name__ == "__main__":
    main()
