# -*- coding: utf-8 -*-

import sys,os
from PyQt5.QtWidgets import QApplication, QWidget,QToolTip,QPushButton,QDesktopWidget,QLabel,QLineEdit,QTextEdit,QGridLayout,QFileDialog
from PyQt5.QtGui import QIcon
import threading


import autosign_duoyouzuan

class HomeView(QWidget):

	def __init__(self): 
		super().__init__()
		# self.fileos_result = os.path.dirname(os.path.realpath(__file__)) + "\\result"
		self.fileos_result = os.path.split(os.path.realpath(__file__))[0]
		print("real local："+self.fileos_result);
		self.initUI()

	def initUI(self):
		tips_apk = QLabel("选择apk")
		tips_keystore  = QLabel("选择keystore")
		tips_password  = QLabel("密码")
		tips_password_2  = QLabel("别名")
		tips_channels = QLabel("输入渠道")


		self.btn_apk =  QPushButton("选择apk文件",self)
		self.btn_keystore =  QPushButton("选择签名keystore文件",self)
		self.ed_password =  QLineEdit('qq123123')
		self.ed_bieming =  QLineEdit('luori')
		self.ed_channels =  QTextEdit('baidu')

		self.btn = QPushButton('开始打包',self)

		self.btn_apk.clicked.connect(self.btn_apk_Clicked)            
		self.btn_keystore.clicked.connect(self.btn_keystore_Clicked)
		self.btn.clicked.connect(self.btn_ok_Clicked)

		grid = QGridLayout()
		grid.setSpacing(10)

		grid.addWidget(tips_apk,1,0)
		grid.addWidget(self.btn_apk,1,1)

		grid.addWidget(tips_keystore,2,0)
		grid.addWidget(self.btn_keystore,2,1)

		grid.addWidget(tips_password,3,0)
		grid.addWidget(self.ed_password,3,1)

		grid.addWidget(tips_password_2,4,0)
		grid.addWidget(self.ed_bieming,4,1)

		grid.addWidget(tips_channels,5,0)
		grid.addWidget(self.ed_channels,5,1,10,1)

		grid.addWidget(self.btn,15,0)

		self.setLayout(grid)
		self.resize(250,150)
		self.setMinimumSize(266, 354); 
		self.setMaximumSize(266, 354);
		self.center()
		self.setWindowTitle('AutoSign 1.0')
		self.setWindowIcon(QIcon('icon/icon.ico'))
		self.show()

	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def btn_apk_Clicked(self):
		filename,_ = QFileDialog.getOpenFileName(self);
		# text=open(filename,'r').read()
		self.btn_apk.setText(filename)

	def btn_keystore_Clicked(self):
		filename,_ = QFileDialog.getOpenFileName(self);
		# text=open(filename,'r').read()
		self.btn_keystore.setText(filename)

	def btn_ok_Clicked(self):
		filename_apk = self.btn_apk.text()
		filename_keystore = self.btn_keystore.text()
		password = self.ed_password.text()
		bieming = self.ed_bieming.text()
		text_channels = self.ed_channels.toPlainText().split("\n")

		autosign_duoyouzuan.filename_apk = filename_apk
		autosign_duoyouzuan.filename_keystore = filename_keystore
		autosign_duoyouzuan.filename_result = self.fileos_result+"\\result"
		autosign_duoyouzuan.keystore_password = password.strip()
		autosign_duoyouzuan.keystore_bieming = bieming.strip()
		autosign_duoyouzuan.text_channels = text_channels
		autosign_duoyouzuan.real_path = self.fileos_result

		# autosign_duoyouzuan.initItem

		threads = []
		t1 = threading.Thread(target=autosign_duoyouzuan.initItem)
		t1.setDaemon(True)
		t1.start()


		print(autosign_duoyouzuan.text_channels)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	hv = HomeView()
	sys.exit(app.exec_())

