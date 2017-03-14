#FileName:lean001.py
#author:www.py40.com

#执行os命令
import os
import shutil
import sys

# path_item = sys.path[0]
filename_apk =''
filename_keystore = ''
filename_result = ''
keystore_password = 'aa123456'
keystore_bieming = 'autosign'
text_channels = []

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
	print('删除过期文件'+filename_result+'/apk')
	shutil.rmtree(filename_result+'/apk',True)
	path_apk_old  = 'apktool d '+filename_apk+' -o ' +filename_result+'/apk'
	os.system(path_apk_old)	
	print('反编译apk文件成功：'+filename_result)	


def signApk():
	print('开始回编译打包')
	apk_back = 'apktool b '+filename_result+"/apk"
	os.system(apk_back)
	print('回编译打包成功')
	print('开始执行自动签名任务')
	signapkcommond = 'jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore '+filename_keystore+' -storepass '+ keystore_password+' '+ filename_result+'/apk/dist/app.apk '+keystore_bieming;
	print('签名命令:'+signapkcommond)
	os.system(signapkcommond)
	print('签名成功')

def initItem():
	#删除appresult文件夹
	print('清除appresult文件夹')
	shutil.rmtree(filename_result,True)

	#创建appresult文件夹
	print('创建appresult文件夹')
	os.makedirs(filename_result)
	
	for line_item in text_channels:
		if not line_item:
			continue
		print(line_item)
		decomApk()
		print('开始修改apk内容')
		fileManifest = filename_result+"/apk/AndroidManifest.xml"
		modifyFile(fileManifest,'Duoyou_qudao',line_item)
		signApk()
		shutil.copy(filename_result+"/apk/dist/app.apk", filename_result)
		print('文件复制成功')
		new_app_name = 'app_'+line_item+'.apk'
		print("文件名修改为：",new_app_name)
		os.rename(filename_result+"/app.apk", filename_result+"/"+new_app_name)


# print("当前目录为："+path_item)
# initItem()
# print("脚本执行结束：")