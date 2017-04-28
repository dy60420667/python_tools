import requests,time
from PyQt5.QtWidgets import QApplication


class UtilsRequest():
    #联网超时时间
    time_out = 30

    #联网失败重试次数
    request_nums = 5;

    is_pasue = False;

    def __init__(self):
        super().__init__();

    def requestpageText(self,url):
        if self.is_pasue:
            return;

        request_count = self.request_nums
        try:
            request_count-=1
            head = {
                'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

            Page = requests.session().get(url, headers=head, timeout=self.time_out)
            Page.encoding = "utf-8"
            QApplication.processEvents()
            print("获取网页数据成功")
            return Page.text
        except Exception as e:
            print("联网失败了...重试中", e)
            time.sleep(5)
            print("暂停结束")
            if request_count >=0 :
                    self.requestpageText(url)

    def downfile(self,file, url):
        if self.is_pasue:
            return;

        print("开始下载：", file, url)
        try:
            r = requests.get(url, stream=True)
            with open(file, 'wb') as fd:
                for chunk in r.iter_content():
                    fd.write(chunk)
                    QApplication.processEvents()
        except Exception as e:
            print("下载失败了", e)