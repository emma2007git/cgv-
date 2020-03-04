# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
import os.path
import requests
from selenium import webdriver

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):

        self.id_pw_file = "C:/Users/강민주/cgv 커플링클럽 자동 출첵/id_pw.txt"
        
        if os.path.isfile(self.id_pw_file):
            self.state = 1
            print("파일 존재")
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
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(120, 130, 261, 31))
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(80, 140, 21, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(70, 190, 31, 16))
        self.label_4.setObjectName("label_4")
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
        self.label_2.setText(_translate("Dialog", "최초 실행이므로 cgv에 로그인해야됩니다."))
        self.label_3.setText(_translate("Dialog", "ID"))
        self.label_4.setText(_translate("Dialog", "PW"))
        self.pushButton.setText(_translate("Dialog", "확인"))

    def login(self):
        str_id = 'ctl00$mainContentPlaceHolder$Login$tbUserID'
        str_pw = 'ctl00$mainContentPlaceHolder$Login$tbPassword'

        my_id = self.textEdit.toPlainText()
        my_pw = self.textEdit_2.toPlainText()

        LOGIN_INFO = {
            str_id: my_id,
            str_pw : my_pw
        }
        
        # 강민주 부분을 사용자 이름으로 대체하게 하기
        driver = webdriver.Chrome("C:/Users/강민주/Downloads/chromedriver_win32/chromedriver.exe")
        driver.implicitly_wait(3)

        # cgv 로그인
        driver.get('http://m.cgv.co.kr/WebApp/Member/Login.aspx?RedirectURL=http%3A%2F%2Fm.cgv.co.kr%2FWebApp%2FMyCgvV5%2FmyMain.aspx')

        driver.find_element_by_name(str_id).send_keys(LOGIN_INFO[str_id])
        driver.find_element_by_name(str_pw).send_keys(LOGIN_INFO[str_pw])

        # 광고페이지 스킵
        #if driver.find_element_by_xpath('//*[@id="ContainerView"]/div/div/div/div[1]/div[5]/button').is_displayed:
        driver.find_element_by_xpath('//*[@id="ContainerView"]/div/div/div/div[1]/div[5]/button').click()

        # 출석 체크!!
        driver.get('http://m.cgv.co.kr/WebApp/Club/Coupling/MyCoupleActivity.aspx')
        
        driver.find_element_by_xpath('/html/body/div[1]/a[1]').click()       
 
        driver.find_element_by_xpath('//*[@id="ContainerView"]/div[2]/div/div[2]/div[2]/button').click()


        driver.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
