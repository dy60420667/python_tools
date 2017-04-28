# -*- coding: utf-8 -*-
'''
auth:py40.com
download picture from huaban
'''

import sys,os
import threading
import webbrowser

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget,QTextBrowser, QPushButton,QDesktopWidget,QLabel,QLineEdit,QTextEdit,QCheckBox,QGridLayout,QFileDialog,QVBoxLayout,QMessageBox

import Huaban



class DownloadHuaban(QWidget):
    current_file_dictory = ""
    huban = ''
    item_name = "花瓣网图片下载器 1.0"

    def __init__(self):
        super().__init__()
        self.current_file_dictory = os.path.split(os.path.realpath(__file__))[0]
        self.huban = Huaban.Huaban()
        self.initUI()

    def initUI(self):
        tips = QLabel("作者：大猫");
        self.tips_1 = QLabel("网站：<a href='http://py40.com'>http://py40.com</a>");
        self.tips_1.setOpenExternalLinks(True)
        tips_null=QLabel();

        gridDescript = QGridLayout()
        gridDescript.addWidget(tips, 1, 0)
        gridDescript.addWidget(self.tips_1, 2, 0)
        gridDescript.addWidget(tips_null, 3, 0)
        gridDescript.addWidget(tips_null, 4, 0)

        tips_savefile = QLabel("图片保存路径")
        tips_key  = QLabel("搜索关键字")
        tips_guolv = QLabel("是否过滤掉普通图片")

        self.btn_savefile =  QPushButton(self.huban.file_save_path,self)
        self.ed_bieming =  QLineEdit('花瓣')
        self.cb_guolv =  QCheckBox()

        self.btn_ok = QPushButton('开始下载',self)
        self.btn_pause = QPushButton('暂停下载', self)

        self.btn_savefile.clicked.connect(self.btn_savefile_Clicked)
        self.btn_ok.clicked.connect(self.btn_ok_Clicked)
        self.btn_pause.clicked.connect(self.btn_pause_Clicked)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(tips_savefile,1,0)
        grid.addWidget(self.btn_savefile,1,1)


        grid.addWidget(tips_key,2,0)
        grid.addWidget(self.ed_bieming,2,1)

        grid.addWidget(tips_guolv,3,0)
        grid.addWidget(self.cb_guolv,3,1)

        grid.addWidget(tips_null, 4, 0)

        gridBtn = QGridLayout()
        gridBtn.setSpacing(10)

        gridBtn.addWidget(self.btn_ok, 1, 0)
        gridBtn.addWidget(self.btn_pause, 1, 1)

        vbox = QVBoxLayout()
        vbox.addLayout(gridDescript)
        vbox.addLayout(grid)
        vbox.addLayout(gridBtn)

        self.setLayout(vbox)

        self.resize(250,150)
        self.center()
        self.setWindowTitle(self.item_name)
        self.setWindowIcon(QIcon('icon/icon.ico'))
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def btn_savefile_Clicked(self):
        filename= QFileDialog.getExistingDirectory(self,directory=self.huban.file_save_path);
        print(filename)
        # text=open(filename,'r').read()
        self.btn_savefile.setText(filename)

    def btn_pause_Clicked(self):
        self.huban.stopDownLoadHuban()
        self.showTipsDialog(text="下载已暂停")


    def btn_ok_Clicked(self):
        print("oncliuck")
        self.huban.ru.is_pasue = False
        self.huban.down_photo_num = 0
        self.huban.page_nums = 0

        save_file = self.btn_savefile.text();
        if save_file:
            self.huban.file_save_path =save_file

        self.huban.text_keyword = self.ed_bieming.text();

        self.t1 = threading.Thread(target=self.huban.downloadhuaban())
        self.t1.setDaemon(True)
        self.t1.start()

    def showTipsDialog(self, text):
        try:
            QMessageBox.about(self, "提示", text).show()
        except Exception as e:
            print(e)

    def tips_1_Clicked(self,url):
        webbrowser.open("http://py40.com")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = DownloadHuaban()
    sys.exit(app.exec_())

