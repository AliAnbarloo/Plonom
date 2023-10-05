from PyQt5 import QtWidgets, uic
import os
import UserAuthentication

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # بارگذاری اولین فایل UI
        uic.loadUi('/home/ubuntu/نوشتارها/Plonom_Start.ui', self)

        # اتصال دکمه به تابع
        self.Start_Plonom.clicked.connect(self.button_clicked)

        # ایجاد ویژگی برای ذخیره UI جاری
        self.current_ui = None

    def button_clicked(self):
        # ایجاد یک شیء جدید از کلاس طراحی شده توسط Qt Designer
        new_ui = uic.loadUi('/home/ubuntu/نوشتارها/Plonom_Email.ui', self)

        # نمایش فرم جدید
        new_ui.Submit.clicked.connect(self.confirm_button_clicked)
        new_ui.show()

        # ذخیره UI جاری
        self.current_ui = new_ui

    def confirm_button_clicked(self):
        # دسترسی به QLineEdit در UI دوم و ذخیره محتوا در متغیر
        line_edit_content = self.current_ui.Email_input.text()

        x = UserAuthentication.pass_gen()
        UserAuthentication.Send_Email(reciver=line_edit_content, verification_Code=x)
        print("email send!")

        # حذف UI جاری
        self.current_ui.close()

        # ایجاد یک شیء جدید از کلاس دیگر
        login_ui = uic.loadUi("/home/ubuntu/نوشتارها/login_with_email.ui", self)

        # نمایش فرم جدید
        login_ui.show()

        # اتصال دکمه Continue به تابع Login_To_App
        login_ui.Continue.clicked.connect(self.Login_To_App)

    def Login_To_App(self):
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

#/home/ubuntu/نوشتارها/Plonom_Start.ui
#/home/ubuntu/نوشتارها/Polonom_Email.ui