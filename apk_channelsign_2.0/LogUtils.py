#日志管理类

class LogUtils():
    log_items = [];
    log_result = 0;

    def ___init__(self):
        super().__init__()
        self.initData()

    def appendLogItem(self,item):
        self.log_items.append(item)
        if item!=0:
            print("**************注意脚本执行错误******")

    def startLog(self):
        self.log_result = 1;
        print('**************开始记录日志*****************')

    def stopLog(self):
        self.log_result = 2;
        print('**************终止记录日志*****************')

    def getLogItems(self):
        return self.log_items;

    #判断脚本是否执行成功
    def itemIsSucess(self):
        if len(self.log_items) == 0:
            return False;
        for x in self.log_items:
            if x!=0:
                return False;
        return True;

    #脚本是否正在执行
    def itemIsLoading(self):
        print("验证脚本是否正在执行:",self.log_result)
        if self.log_result==1:
            return True
        else:
            return False;

    def checkThred(self):
        if self.itemIsSucess():
            print('*****************************脚本执行成功了*****************************')
            return True
        else:
            print('*****************************验证脚本执行失败了*****************************')
            return False

    def initDate(self):
        print('日志初始化')
        self.log_items = []  # 里面的每一项如果都为0表示某一项任务执行成功
        self.log_result = 0  # 0代表脚本未开始执行，1表示脚本执行中，2表示脚本执行结束
