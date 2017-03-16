# -*- coding: utf-8 -*-

import os
import sys
import threading
import time

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QDesktopWidget,QLabel,QLineEdit,QTextEdit,QGridLayout,QFileDialog,QVBoxLayout,QMessageBox

import AutoSign
import LogUtils
import CacheUtils

item_name = "APK Channels 2.0"

class PageChangeChannels(QWidget):
	logutil =""
	autosign = ""
	current_file_dictory = ""
	cacheUtils = ''


	def __init__(self): 
		super().__init__()
		self.current_file_dictory = os.path.split(os.path.realpath(__file__))[0]
		self.autosign = AutoSign.AutoSign()

		self.cacheUtils = CacheUtils.CacheUtils()
		self.cacheUtils.init(self.current_file_dictory)

		self.logutil = LogUtils.LogUtils()
		self.autosign.logUtil = self.logutil;
		self.autosign.page_changechannels = self;
		print("real local："+self.current_file_dictory);
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

		self.btn_ok = QPushButton('开始打包',self)

		self.btn_apk.clicked.connect(self.btn_apk_Clicked)            
		self.btn_keystore.clicked.connect(self.btn_keystore_Clicked)
		self.btn_ok.clicked.connect(self.btn_ok_Clicked)

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

		gridBtn = QGridLayout()
		gridBtn.setSpacing(10)

		gridBtn.addWidget(self.btn_ok, 1, 0)


		vbox = QVBoxLayout()
		vbox.addLayout(grid)
		vbox.addLayout(gridBtn)
		# vbox.addWidget(grid)
		# vbox.addWidget(self.btn_ok)

		# grid.addWidget(self.btn,15,0)
		# self.setLayout(grid)
		self.setLayout(vbox)

		self.resize(250,150)
		self.setMinimumSize(266, 354); 
		self.setMaximumSize(266, 354);
		self.center()
		self.setWindowTitle(item_name)
		self.setWindowIcon(QIcon('icon/icon.ico'))
		self.show()

	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def btn_apk_Clicked(self):
		apk_file  = self.cacheUtils.getCacheString('apk_file',self.current_file_dictory)
		filename,_ = QFileDialog.getOpenFileName(self,apk_file);
		# text=open(filename,'r').read()
		self.btn_apk.setText(filename)
		self.cacheUtils.setCacheString('apk_file', filename)

	def btn_keystore_Clicked(self):
		key_store = self.cacheUtils.getCacheString('key_store',self.current_file_dictory)
		filename,_ = QFileDialog.getOpenFileName(self,key_store);
		# text=open(filename,'r').read()
		self.btn_keystore.setText(filename)
		self.cacheUtils.setCacheString('key_store', filename)

	def btn_ok_Clicked(self):
		if  self.logutil.itemIsLoading():
			return;
		else:
			self.autosign.filename_apk = self.btn_apk.text()
			self.autosign.filename_keystore = self.btn_keystore.text()
			self.autosign.filename_result = self.current_file_dictory + "\\result"
			self.autosign.keystore_password = self.ed_password.text().strip()
			self.autosign.keystore_bieming = self.ed_bieming.text().strip()
			self.autosign.text_channels = self.ed_channels.toPlainText().split("\n")
			self.autosign.real_path = self.current_file_dictory

			self.t1 = threading.Thread(target=self.autosign.autoSign())
			self.t1.setDaemon(True)
			self.t1.start()

	def showTipsDialog(self,text):
		try:
			QMessageBox.about(self,"提示", text).show()
		except Exception as e:
			print(e)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	hv = PageChangeChannels()
	sys.exit(app.exec_())

