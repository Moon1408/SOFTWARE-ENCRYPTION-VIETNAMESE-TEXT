import sys
sys.path.append("D:/HUFLIT/Nam3/BMHTTT/DoAN/Control")
from PyQt6.QtWidgets import QApplication, QMainWindow
from ThietKe.ThietKeManHinhChinh import Ui_MainWindow
from GiaoDienLoginDialog import LoginDialog
from GiaoDienSignupDialog import SignupDialog


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_DangNhap.clicked.connect(self.on_Login_click)
        self.btn_DangKy.clicked.connect(self.on_Signup_click)
        
    def on_Login_click(self):
        self.login_window = LoginDialog()
        # Kết nối tín hiệu từ Dialog với khe (slot) của MainWindow
        #self.login_window.data_signal.connect(self.receive_data_from_dialog)
        self.login_window.show() #mở màn hình login

    def on_Signup_click(self):
        self.Signup_window = SignupDialog()
        self.Signup_window.show() #mở màn hình login

    ''' def receive_data_from_dialog(self, data):
    #print(f"Received data from Dialog: {data}")
        if data == 'ok':         
            self.menuM_ho.setEnabled(True)
            self.menuGi_i_m.setEnabled(True)
   '''
        
def main():
    app = QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
