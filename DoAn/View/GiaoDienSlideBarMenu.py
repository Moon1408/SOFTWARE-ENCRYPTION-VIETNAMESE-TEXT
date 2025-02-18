import sys
sys.path.append("D:/HUFLIT/Nam3/BMHTTT/DoAN/Control")
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from ThietKe.ThietKeSlideBarMenu import Ui_OtherWindow

from GiaoDienMaHoaCeasar import MyMHCeasar
from GiaoDienGiaiMaCeasar import MyGMCeasar
from GiaoDienMaHoaVignere import MyMHVignere
from GiaoDienGiaiMaVignere import MyGMVignere
from GiaoDienMaHoaTrithemius import MyMHTrithemius
from GiaoDienGiaiMaTrithemius import MyGMTrithemius

from GiaoDienMaHoaBelasco import MyMHBelasco
from GiaoDienGiaiMaBelasco import MyGMBelasco
from GiaoDienMaHoaHaiDong import MyMHHaiDong
from GiaoDienGiaiMaHaiDong import MyGMHaiDong
from GiaoDienMaHoaNhieuDong import MyMHNhieuDong
from GiaoDienGiaiMaNhieuDong import MyGMNhieuDong

from GiaoDienMaHoaXORCeasar import MyMHXORCeasar
from GiaoDienGiaiMaXORCeasar import MyGMXORCeasar
from GiaoDienMaHoaXORVignere import MyMHXORVignere
from GiaoDienGiaiMaXORVignere import MyGMXORVignere 
from GiaoDienMaHoaXORBelasco import MyMHXORBelasco
from GiaoDienGiaiMaXORBelasco import MyGMXORBelasco
from GiaoDienMaHoaXORTrithemius import MyMHXORTrithemius
from GiaoDienGiaiMaXORTrithemius import MyGMXORTrithemius

from GiaoDienMaHoaSDES import MyMHSDES
from GiaoDienGiaiMaSDES import MyGMSDES
from GiaoDienMaHoaRSA import MyMHRSA
from GiaoDienGiaiMaRSA  import MyGMRSA
from GiaoDienMaHoaAES import MyMHAES
from GiaoDienGiaiMaAES import MyGMAES

from GiaoDienMaHoaMD5 import MyMHMD5
from GiaoDienMaHoaSHA3 import MyMHSHA3
from GiaoDienMaHoaSHA256 import MyMHSHA256




####################################################################################
class MyMainWindowSBM(QMainWindow, Ui_OtherWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_OtherWindow()
        self.ui.setupUi(self)

        ## =======================================================================================================
        ## Lấy tất cả các đối tượng trong windows 
        ## =======================================================================================================
        ## Thêm đây nè
        ## Mã hóa 
        self.actionCeasar_MaHoa_btn = self.ui.actionCeasar_MaHoa
        self.actionVignere_MaHoa_btn = self.ui.actionVignere_MaHoa
        self.actionTrithemius_MaHoa_btn = self.ui.actionTrithemius_MaHoa
        self.actionBelasco_MaHoa_btn = self.ui.actionBelasco_MaHoa 
        
        self.actionHai_dong_MaHoa_btn = self.ui.actionHai_dong_MaHoa
        self.actionNhieu_dong_MaHoa_btn = self.ui.actionNhieu_dong_MaHoa
        
        self.actionCeasar_XOR_MaHoa_btn = self.ui.actionCeasar_XOR_MaHoa
        self.actionVignere_XOR_MaHoa_btn = self.ui.actionVignere_XOR_MaHoa
        self.actionTrithemius_XOR_MaHoa_btn = self.ui.actionTrithemius_XOR_MaHoa
        self.actionBelasco_XOR_MaHoa_btn = self.ui.actionBelasco_XOR_MaHoa

        self.actionSDES_MaHoa_btn = self.ui.actionSDES_MaHoa
        self.actionRSA_MaHoa_btn = self.ui.actionRSA_MaHoa
        self.actionAES_MaHoa_btn = self.ui.actionAES_MaHoa
        
        ## Giải mã
        self.actionCeasar_GiaiMa_btn = self.ui.actionCeasar_GiaiMa
        self.actionVignere_GiaiMa_btn = self.ui.actionVignere_GiaiMa
        self.actionTrithemius_GiaiMa_btn = self.ui.actionTrithemius_GiaiMa
        self.actionBelasco_GiaiMa_btn = self.ui.actionBelasco_GiaiMa 
        
        self.actionHai_dong_GiaiMa_btn = self.ui.actionHai_dong_GiaiMa
        self.actionNhieu_dong_GiaiMa_btn = self.ui.actionNhieu_dong_GiaiMa
        
        self.actionCeasar_XOR_GiaiMa_btn = self.ui.actionCeasar_XOR_GiaiMa
        self.actionVignere_XOR_GiaiMa_btn = self.ui.actionVignere_XOR_GiaiMa
        self.actionTrithemius_XOR_GiaiMa_btn = self.ui.actionTrithemius_XOR_GiaiMa
        self.actionBelasco_XOR_GiaiMa_btn = self.ui.actionBelasco_XOR_GiaiMa

        self.actionSDES_GiaiMa_btn = self.ui.actionSDES_GiaiMa
        self.actionRSA_GiaiMa_btn = self.ui.actionRSA_GiaiMa
        self.actionAES_GiaiMa_btn = self.ui.actionAES_GiaiMa 

        self.actionMD5_MaHoa_btn = self.ui.actionMD5_MaHoa
        self.actionSHA3_MaHoa_btn = self.ui.actionSHA3_MaHoa
        self.actionSHA256_MaHoa_btn = self.ui.actionSHA256_MaHoa
        
        ## =======================================================================================================
        ## Tạo dict cho các nút menu và cửa sổ tab
        ## =======================================================================================================
        ## Thêm đây nè 
        self.menu_btns_list = {
            # Mã hóa 
            self.actionCeasar_MaHoa_btn: MyMHCeasar(),
            self.actionVignere_MaHoa_btn: MyMHVignere(), 
            self.actionTrithemius_MaHoa_btn: MyMHTrithemius(),
            self.actionBelasco_MaHoa_btn: MyMHBelasco(),
        
            self.actionHai_dong_MaHoa_btn: MyMHHaiDong(),
            self.actionNhieu_dong_MaHoa_btn: MyMHNhieuDong(),

            self.actionCeasar_XOR_MaHoa_btn: MyMHXORCeasar(),
            self.actionVignere_XOR_MaHoa_btn: MyMHXORVignere(),
            self.actionTrithemius_XOR_MaHoa_btn: MyMHXORTrithemius(),
            self.actionBelasco_XOR_MaHoa_btn: MyMHXORBelasco(),
            
            self.actionSDES_MaHoa_btn: MyMHSDES(),
            self.actionRSA_MaHoa_btn: MyMHRSA(),
            self.actionAES_MaHoa_btn: MyMHAES(),
            
            #Giải mã
            self.actionCeasar_GiaiMa_btn: MyGMCeasar(),
            self.actionVignere_GiaiMa_btn: MyGMVignere(),
            self.actionTrithemius_GiaiMa_btn: MyGMTrithemius(),
            self.actionBelasco_GiaiMa_btn: MyGMBelasco(),
            
            self.actionHai_dong_GiaiMa_btn:  MyGMHaiDong(),
            self.actionNhieu_dong_GiaiMa_btn: MyGMNhieuDong(),

            self.actionCeasar_XOR_GiaiMa_btn: MyGMXORCeasar(),
            self.actionVignere_XOR_GiaiMa_btn: MyGMXORVignere(),
            self.actionTrithemius_XOR_GiaiMa_btn: MyGMXORTrithemius(),
            self.actionBelasco_XOR_GiaiMa_btn: MyGMXORBelasco(),

            self.actionSDES_GiaiMa_btn: MyGMSDES(),
            self.actionRSA_GiaiMa_btn: MyGMRSA(),
            self.actionAES_GiaiMa_btn: MyGMAES(),

            self.actionMD5_MaHoa_btn: MyMHMD5(),
            self.actionSHA3_MaHoa_btn: MyMHSHA3(),
            self.actionSHA256_MaHoa_btn: MyMHSHA256()
            
    
        }
        ## =======================================================================================================
        ## Hiển thị cửa sổ chính khi khởi động ứng dụng
        ## =======================================================================================================
        self.show_home_window()
        self.ui.tabWidget.tabCloseRequested.connect(self.close_tab)
        
        ## =======================================================================================================
        ## Kết nối tín hiệu và khe cắm
        ## =======================================================================================================
        ## Thêm đây nè
        # Mã hóa 
        self.actionCeasar_MaHoa_btn.clicked.connect(self.show_selected_window)        
        self.actionVignere_MaHoa_btn.clicked.connect(self.show_selected_window)
        self.actionTrithemius_MaHoa_btn.clicked.connect(self.show_selected_window)
        self.actionBelasco_MaHoa_btn.clicked.connect(self.show_selected_window)
        
        self.actionHai_dong_MaHoa_btn.clicked.connect(self.show_selected_window)
        self.actionNhieu_dong_MaHoa_btn.clicked.connect(self.show_selected_window)



        self.actionSDES_MaHoa_btn.clicked.connect(self.show_selected_window)
        self.actionRSA_MaHoa_btn.clicked.connect(self.show_selected_window)
        self.actionAES_MaHoa_btn.clicked.connect(self.show_selected_window)
        
        self.actionCeasar_XOR_MaHoa_btn.clicked.connect(self.show_selected_window)
        self.actionVignere_XOR_MaHoa_btn.clicked.connect(self.show_selected_window)
        self.actionTrithemius_XOR_MaHoa_btn.clicked.connect(self.show_selected_window)
        self.actionBelasco_XOR_MaHoa_btn.clicked.connect(self.show_selected_window)


        #Giải mã
        self.actionCeasar_GiaiMa_btn.clicked.connect(self.show_selected_window)
        self.actionVignere_GiaiMa_btn.clicked.connect(self.show_selected_window)
        self.actionTrithemius_GiaiMa_btn.clicked.connect(self.show_selected_window)
        self.actionBelasco_GiaiMa_btn.clicked.connect(self.show_selected_window)
            
        self.actionHai_dong_GiaiMa_btn.clicked.connect(self.show_selected_window)
        self.actionNhieu_dong_GiaiMa_btn.clicked.connect(self.show_selected_window)
            
        self.actionCeasar_XOR_GiaiMa_btn.clicked.connect(self.show_selected_window) 
        self.actionVignere_XOR_GiaiMa_btn.clicked.connect(self.show_selected_window)
        self.actionTrithemius_XOR_GiaiMa_btn.clicked.connect(self.show_selected_window)
        self.actionBelasco_XOR_GiaiMa_btn.clicked.connect(self.show_selected_window)

        self.actionSDES_GiaiMa_btn.clicked.connect(self.show_selected_window) 
        self.actionRSA_GiaiMa_btn.clicked.connect(self.show_selected_window) 
        self.actionAES_GiaiMa_btn.clicked.connect(self.show_selected_window)

        self.actionMD5_MaHoa_btn.clicked.connect(self.show_selected_window) 
        self.actionSHA3_MaHoa_btn.clicked.connect(self.show_selected_window) 
        self.actionSHA256_MaHoa_btn.clicked.connect(self.show_selected_window) 
            

    def show_home_window(self):
        result = self.open_tab_flag(self.actionCeasar_MaHoa_btn.text())
        self.set_btn_checked(self.actionCeasar_MaHoa_btn)

        if result is not None and result[0]:
            self.ui.tabWidget.setCurrentIndex(result[1])
        else:
            title = self.actionCeasar_MaHoa_btn.text()
            curIndex = self.ui.tabWidget.addTab(MyMHCeasar(), title)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            # Kết nối tín hiệu closeTabSignal từ tab mới được thêm vào với hàm close_tab
            self.ui.tabWidget.widget(curIndex).closeTabSignal.connect(lambda: self.close_tab(curIndex))
            self.ui.tabWidget.setVisible(True)
    def show_selected_window(self):
        """
        Function for showing selected window
        :return:
        """
        button = self.sender()
        result = self.open_tab_flag(button.text())
        self.set_btn_checked(button)

        if result[0]:
            self.ui.tabWidget.setCurrentIndex(result[1])
        else:
            title = button.text()
            curIndex = self.ui.tabWidget.addTab(self.menu_btns_list[button], title)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            # Kết nối tín hiệu closeTabSignal từ tab mới được thêm vào với hàm close_tab
            self.ui.tabWidget.widget(curIndex).closeTabSignal.connect(lambda: self.close_tab(curIndex))
            self.ui.tabWidget.setVisible(True)
    # Sửa hàm open_tab_flag để trả về False nếu không tìm thấy tab
    def open_tab_flag(self, tab):
        open_tab_count = self.ui.tabWidget.count()

        for i in range(open_tab_count):
            tab_name = self.ui.tabWidget.tabText(i)
            if tab_name == tab:
                return True, i
        return False, -1  # Trả về giá trị mặc định nếu không tìm thấy tab
    def close_tab(self, index):
        index = self.ui.tabWidget.currentIndex()
        if 0 <= index < self.ui.tabWidget.count():
            if self.ui.tabWidget.currentIndex() == 0:
                self.dong_tab_dau()
            elif index == self.ui.tabWidget.count() - 1:
                self.dong_tab_cuoi()
            else:
                self.dong_tab_bat_ki(index)
        if self.ui.tabWidget.count() == 0:  
            self.close()        
    def dong_tab_dau(self):
        self.ui.tabWidget.removeTab(0)
        if self.ui.tabWidget.count() >= 0:  # Kiểm tra xem còn tab nào không sau khi xóa
            self.ui.tabWidget.setCurrentIndex(0)  # Nếu còn, đặt tab tiếp theo làm tab hiện tại
    def dong_tab_cuoi(self):
        index = self.ui.tabWidget.count() - 1
        self.ui.tabWidget.removeTab(index)
        if self.ui.tabWidget.count() > 0:
            self.ui.tabWidget.setCurrentIndex(index - 1)
    def dong_tab_bat_ki(self, index):
        if 0 <= index < self.ui.tabWidget.count():
            current_index = self.ui.tabWidget.currentIndex()
            # Xác định tab cần xóa và tab tiếp theo trong tabWidget
            tab_to_remove = self.ui.tabWidget.widget(index)
            next_tab = self.ui.tabWidget.widget(index + 1) if index + 1 < self.ui.tabWidget.count() else None
            self.ui.tabWidget.removeTab(index)
            # Kiểm tra xem tab cần xóa có phải là tab liền kề với tab tiếp theo không
            if tab_to_remove == next_tab:
                self.close_tab(current_index)  # Gọi hàm close_tab() nếu tab cần xóa là tab liền kề với tab tiếp theo
                    
    def set_btn_checked(self, btn):
        """
        Set the status of selected button checked and set other buttons' status unchecked
        :param btn: button object
        :return:
        """
        for button in self.menu_btns_list.keys():
            if button != btn:
                button.setChecked(False)
            else:
                button.setChecked(True)
#======================================================================================
def main():
    app = QApplication(sys.argv)
    main_window = MyMainWindowSBM()
    main_window.show()
    sys.exit(app.exec()) 
#=============================================================================
if __name__ == "__main__":
    main()

