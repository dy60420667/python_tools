#缓存管理类

import os

class CacheUtils():
    cache_file_dictory = ''#缓存的文件目录

    def __init__(self):
        super().__init__();

    def  init(self,current_file_dictory):
        self.cache_file_dictory = current_file_dictory+"\\cache"
        # 创建appresult文件夹

        if not os.path.exists(self.cache_file_dictory):
            print('创建appresult文件夹')
            os.makedirs(self.cache_file_dictory)

    def setCacheString(self,key,text):
        key_file = self.cache_file_dictory+"\\key.txt"
        f = open(key_file,'w')
        f.write(text)
        f.close()

    def getCacheString(self,key,defaultValue):
        key_file = self.cache_file_dictory + "\\key.txt"
        f = open(key_file, 'r')
        value = f.read()
        f.close()
        if not value:
            return value;
        else:
            return defaultValue;