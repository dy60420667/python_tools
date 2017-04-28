import os
import sys
import re

path = r'C:\Users\Administrator\Desktop\ewwordk'

for (path,dirs,files) in os.walk(path):
    for filename in files:
    	print(filename)
    	matchObj  = re.match("Compress_", filename, flags=0)
    	if(matchObj):
    		print(matchObj.span()[1])
    		newname = filename[matchObj.span()[1]:]
    		print("newName:",newname)
    		os.rename(path+"\\"+filename , path+"\\"+newname)