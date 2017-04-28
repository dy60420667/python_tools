import re,os

import UtilsRequest

class Huaban():
    file_save_path = "D:/work/python/image"
    text_keyword = "航空";
    page_nums = 0;
    down_photo_num=0#下载的图片数量
    ru = ""

    def __init__(self):
        super().__init__();
        self.ru = UtilsRequest.UtilsRequest()

    def downloadhuaban(self):
        if self.ru.is_pasue:
            return
        urlhuaban = "http://huaban.com/search/?q=%s&per_page=20&wfl=1&page=%d"
        urlhuaban = urlhuaban % (self.text_keyword,self.page_nums);
        file_save_path = self.file_save_path+"/"+self.text_keyword+"/";

        print("*******************************************************************")
        print("请求网址：", urlhuaban)

        self.page_nums += 1
        if not os.path.exists(file_save_path):
            os.makedirs(file_save_path)

        text = self.ru.requestpageText(urlhuaban)
        pattern = re.compile('{"pin_id":(\d*?),.*?"key":"(.*?)",.*?"like_count":(\d*?),.*?"repin_count":(\d*?),.*?}',
                             re.S)
        items = re.findall(pattern, text)
        if(len(items)==0):
            print("*******************************************************************")
            print("共下载图片%d张"%self.down_photo_num)
            print("下载资源结束~~~~~~~~~~~~~或未找到资源")
            return;

        print(items)
        for item in items:
            max_pin_id = item[0]
            x_key = item[1]
            x_like_count = int(item[2])
            x_repin_count = int(item[3])
            if (x_repin_count > 10 and x_like_count > 10) or x_repin_count > 10 or x_like_count > 1:
                print("开始下载第{0}张图片".format(self.down_photo_num))

                url_image = "http://hbimg.b0.upaiyun.com/"
                url_item = url_image + x_key
                filename = file_save_path + str(x_key) + ".jpg"
                if os.path.isfile(filename):
                    print("文件存在：", filename)
                    continue

                self.ru.downfile(filename, url_item)
                self.down_photo_num += 1
        self.downloadhuaban()


    def stopDownLoadHuban(self):
        self.ru.is_pasue = True









