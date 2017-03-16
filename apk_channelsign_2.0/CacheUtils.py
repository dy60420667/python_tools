#缓存管理类


class CacheUtils():
    current_file_dictory = ''#缓存的文件目录

    def __init__(self):
        super().__init__();

    def  init(self,current_file_dictory):
        self.current_file_dictory = current_file_dictory

    def setCacheString(self,key,text):
        f = file(self.current_file_dictory+"\\key",'w+')