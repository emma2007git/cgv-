# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
import os.path
import requests
from selenium import webdriver
import getpass

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):

        self.id_pw_file = "C:/Users/{}/cgv 커플링클럽 자동 출첵/id_pw.txt".format(getpass.getuser())
        
        if os.path.isfile(self.id_pw_file):
            self.state = 1
            print("파일 존재")

            f = open(self.id_pw_file,"r")
            self.my_id = f.readline()
            self.my_pw = f.readline()
            f.close()
        else:
            self.state = 0
            print("최초 로그인")

        Dialog.setObjectName("Dialog")
        Dialog.resize(482, 356)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 20, 191, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 80, 281, 20))
        self.label_2.setObjectName("label_2")

        if self.state == 0:
            self.textEdit = QtWidgets.QTextEdit(Dialog)
            self.textEdit.setGeometry(QtCore.QRect(120, 130, 261, 31))
            self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(80, 140, 21, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(70, 190, 31, 16))
        self.label_4.setObjectName("label_4")

        if self.state == 0:
            self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
            self.textEdit_2.setGeometry(QtCore.QRect(120, 190, 261, 31))
            self.textEdit_2.setObjectName("textEdit_2")

            self.pushButton = QtWidgets.QPushButton(Dialog)
            self.pushButton.setGeometry(QtCore.QRect(200, 260, 93, 28))
            self.pushButton.setObjectName("pushButton")
        
            # 확인 버튼 누르면 로그인됨
            self.pushButton.clicked.connect(lambda : self.login())
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "CGV 커플링 클럽 자동 출첵!!"))

        if self.state == 0:
            self.label_2.setText(_translate("Dialog", "최초 실행이므로 cgv에 로그인해야됩니다."))
            self.label_3.setText(_translate("Dialog", "ID"))
            self.label_4.setText(_translate("Dialog", "PW"))
            self.pushButton.setText(_translate("Dialog", "확인"))
        else:
            self.label_2.setText(_translate("Dialog", "                 자동로그인"))

    def login(self):
        str_id = 'ctl00$mainContentPlaceHolder$Login$tbUserID'
        str_pw = 'ctl00$mainContentPlaceHolder$Login$tbPassword'

        # 최초 로그인일 때만 아이디와 비밀번호 입력 
        if self.state == 0:
            self.my_id = self.textEdit.toPlainText()
            self.my_pw = self.textEdit_2.toPlainText()

            f = open(self.id_pw_file,"w")
            f.write(self.my_id + "\n")
            f.write(self.my_pw)
            f.close()
        
        LOGIN_INFO = {
            str_id: self.my_id,
            str_pw : self.my_pw
        }

        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument("--disable-gpu")
        options.add_argument("lang=ko_KR")

        driver = webdriver.Chrome("C:/Users/{}/Downloads/chromedriver_win32/chromedriver.exe".format(getpass.getuser()),chrome_options=options)
        #driver = webdriver.Chrome("C:/Users/{}/Downloads/chromedriver_win32/chromedriver.exe".format(getpass.getuser()))
        driver.implicitly_wait(3)
        
        # cgv 로그인
        driver.get('http://m.cgv.co.kr/WebApp/Member/Login.aspx?RedirectURL=http%3A%2F%2Fm.cgv.co.kr%2FWebApp%2FMyCgvV5%2FmyMain.aspx')

        driver.find_element_by_name(str_id).send_keys(LOGIN_INFO[str_id])
        driver.find_element_by_name(str_pw).send_keys(LOGIN_INFO[str_pw])

        driver.get_screenshot_as_file('cgv.png')

        # 광고페이지 스킵
        #if driver.find_element_by_xpath('//*[@id="ContainerView"]/div/div/div/div[1]/div[5]/button').is_displayed:
        driver.find_element_by_xpath('//*[@id="ContainerView"]/div/div/div/div[1]/div[5]/button').click()

        driver.get_screenshot_as_file('cgv2.png')

        # 출석 체크!!
        driver.get('http://m.cgv.co.kr/WebApp/Club/Coupling/MyCoupleActivity.aspx')
        
        driver.find_element_by_xpath('/html/body/div[1]/a[1]').click()       
 
        driver.get_screenshot_as_file('cgv3.png')

        driver.find_element_by_xpath('//*[@id="ContainerView"]/div[2]/div/div[2]/div[2]/button').click()
         
        

        driver.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()

    if ui.state == 1:
        ui.login()
    sys.exit(app.exec_())
