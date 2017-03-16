#FileName:lean001.py
#author:www.py40.com

#执行os命令
import os
import shutil
import pygame

# path_item = sys.path[0]
class AutoSign():
	real_path = ''
	filename_apk = ''
	filename_keystore = ''
	filename_result = ''
	keystore_password = 'aa123456'
	keystore_bieming = 'autosign'
	text_channels = []
	logUtil = ''
	page_changechannels = ''

	def __init__(self):
		super().__init__();

	def modifyFile(self,tfile,sstr,rstr):
		print('开始修改文件'+tfile)
		print('原始内容'+sstr)
		print('替换内容'+rstr)
		try:
			lines=open(tfile,'r',encoding='utf-8').readlines()
			flen=len(lines)
			for i in range(flen):
				if sstr in lines[i]:
					lines[i]=lines[i].replace(sstr,rstr)
			open(tfile,'w',encoding='utf-8').writelines(lines)
			print('修改文件内容成功：'+rstr)
		except IOError:
			print('输入输出异常')
		except Exception as e:
			print(e)
			print('修改内容失败')


	#反编译apk
	def decomApk(self):
		#删除过期文件
		print('删除过期文件'+self.filename_result+'\\apk')
		shutil.rmtree(self.filename_result+'\\apk',True)
		# fileos = os.path.dirname(os.path.realpath(__file__))
		print('当前路径为：'+self.real_path)
		path_apk_old = self.real_path +'\\apktool_2.2.1\\apktool d '+self.filename_apk+' -o ' +self.filename_result+'\\apk'
		print('执行命令：'+path_apk_old)
		commond_result = os.system(path_apk_old)
		self.logUtil.appendLogItem(commond_result);
		print('反编译apk文件成功：'+self.filename_result)


	def signApk(self):
		print('开始回编译打包')
		# fileos = os.path.dirname(os.path.realpath(__file__))
		apk_back = self.real_path +'\\apktool_2.2.1\\apktool b '+self.filename_result+"\\apk"
		print('执行命令：'+apk_back)
		os.system(apk_back)
		print('回编译打包成功')
		print('开始执行自动签名任务')
		signapkcommond = 'jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore '+self.filename_keystore+' -storepass '+ self.keystore_password+' '+ self.filename_result+'\\apk\\dist\\app.apk '+self.keystore_bieming;
		print('签名命令:'+signapkcommond)
		commond_result = os.system(signapkcommond)
		self.logUtil.appendLogItem(commond_result);
		print('签名结果:',self.logUtil.getLogItems())
		print('签名成功')

	def copyAndChangeTheApp(self):
		print("创建old文件夹")
		os.makedirs(self.filename_result+"\\old\\")
		shutil.copy(self.filename_apk, self.filename_result+"\\old\\app.apk")
		self.filename_apk = self.filename_result+"\\old\\app.apk";


	def initItem(self):
		#删除appresult文件夹
		print('清除appresult文件夹:'+self.filename_result)
		shutil.rmtree(self.filename_result,True)

		#创建appresult文件夹
		print('创建appresult文件夹')
		os.makedirs(self.filename_result)

		self.copyAndChangeTheApp();

		print(self.text_channels)

		for line_item in self.text_channels:
			line_item = line_item.strip()
			if not line_item:
				continue
			print(line_item)
			self.decomApk()
			print('开始修改apk内容')
			fileManifest = self.filename_result+"\\apk\\AndroidManifest.xml"
			self.modifyFile(fileManifest,'Duoyou_qudao',line_item)
			self.signApk()
			shutil.copy(self.filename_result+"\\apk\\dist\\app.apk", self.filename_result)
			print('文件复制成功')
			new_app_name = 'app_'+line_item+'.apk'
			print("文件名修改为：",new_app_name)
			os.rename(self.filename_result+"\\app.apk", self.filename_result+"\\"+new_app_name)

	def autoSign(self):
		text_result = "打包出错了\n请仔细检查信息填写是否完整\n如果依然无法解决请联系作者。"
		try:
			self.logUtil.initDate()
			self.logUtil.startLog()
			self.initItem();
			if self.logUtil.checkThred():
				text_result = '****恭喜脚本执行成功****'
		except Exception as e :
			print(e)
			print('出错了')

		self.logUtil.stopLog()
		self.playVoice();
		self.page_changechannels.showTipsDialog(text_result)


	def playVoice(self):
		print('播放音乐')
		voice = '.\\raw\\playend.mp3'
		pygame.mixer.init()
		track = pygame.mixer.music.load(voice)
		pygame.mixer.music.play()




