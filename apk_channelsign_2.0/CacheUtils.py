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
        print("写入文件：", text)
        key_file = self.cache_file_dictory+"\\"+key+".txt"
        f = open(key_file,'w+')
        f.write(text)
        f.close()

    def getCacheString(self,key,defaultValue):
        key_file = self.cache_file_dictory + "\\"+key+".txt"
        print("获取文件：",key_file)
        if not os.path.exists(key_file):
            print('文件不存在，返回默认值',defaultValue)
            return defaultValue
        else:
            f = open(key_file, 'r')
            value = f.read()
            f.close()
            if value:
                print('获取结果',value)
                return value;
            else:
                print('结果不存在',defaultValue)
                return defaultValue;