import os
import shutil
import sys
import json

path_item = sys.path[0]
path_apk_folder =path_item+'\\apk'


#反编译apk
def decomApk(rfile,tfile):	
	print('源文件：'+rfile)
	print('存文件：'+tfile)
	path_apk_old  = 'apktool d '+rfile +' -o ' +tfile
	os.system(path_apk_old)	
	print('反编译apk文件成功：'+path_apk_folder)	


def initItem():
	for filedapp in os.listdir(path_item+"\\appresult"):
		print(filedapp)
		decomApk(path_item+"\\appresult\\"+filedapp,path_item+"\\appresult\\"+filedapp[:-4])


initItem()
print('反编译结束，请查看manifest文件')
