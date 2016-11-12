#FileName:lean001.py
#author:www.py40.com

#执行os命令
import os
import shutil
import sys

path_item = sys.path[0]
path_apk_folder =path_item+'\\apk'
keystore_password = 'aa123456'
keystore_bieming = 'autosign'
keystore_name = 'autosign_aa123456.jks'
listqudao = []

def modifyFile(tfile,sstr,rstr):
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
def decomApk():	
	#删除过期文件
	print('删除过期文件'+path_apk_folder)
	shutil.rmtree(path_apk_folder,True)
	path_apk_old  = 'apktool d '+path_item+'\\app.apk -o ' +path_apk_folder
	os.system(path_apk_old)	
	print('反编译apk文件成功：'+path_apk_folder)	


def signApk():
	print('开始回编译打包')
	apk_back = 'apktool b '+path_item+"\\apk"
	os.system(apk_back)
	print('回编译打包成功')
	print('开始执行自动签名任务')
	signapkcommond = 'jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore '+path_item+'\\'+keystore_name+' -storepass '+ keystore_password+' '+ path_item+'\\apk\\dist\\app.apk '+keystore_bieming;
	print('签名命令:'+signapkcommond)
	os.system(signapkcommond)
	print('签名成功')

def initItem():
	
	#删除appresult文件夹
	print('清除appresult文件夹')
	shutil.rmtree(path_item+"\\appresult",True)

	#创建appresult文件夹
	print('创建appresult文件夹')
	os.makedirs(path_item+"\\appresult")

	lines=open(path_item+"\\qudao.txt",'r',encoding='utf-8').readlines()
	for line_item in lines:
		line_item=line_item.strip('\n')
		if not line_item:
			continue
		print(line_item)
		decomApk()
		print('开始修改apk内容')
		fileManifest = path_apk_folder+"\\AndroidManifest.xml"
		modifyFile(fileManifest,'Duoyou_qudao',line_item)
		signApk()
		shutil.copy(path_item+"\\apk\\dist\\app.apk", path_item+"\\appresult")
		print('文件复制成功')
		new_app_name = 'app_'+line_item+'.apk'
		print("文件名修改为：",new_app_name)
		os.rename(path_item+"\\appresult\\app.apk", path_item+"\\appresult\\"+new_app_name)


print("当前目录为："+path_item)
initItem()
print("脚本执行结束：")