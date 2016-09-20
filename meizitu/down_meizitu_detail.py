
import re
import os
import requests

head = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
TimeOut = 30

global PhotoName
PhotoName = 0
PWD="E:/meizitu/pic/"

def requestpageText(url):
    try:
      Page = requests.session().get(url,headers=head,timeout=TimeOut)
      Page.encoding = "gb2312"
      return Page.text
    except BaseException as e:
      print("联网失败了...",e)

def downfile(file,url):
    print("开始下载：",file,url)
    r = requests.get(url,stream=True)
    with open(file, 'wb') as fd:
        for chunk in r.iter_content():
          fd.write(chunk)


def getImageDetail(url):
  	global PhotoName
  	item_start = url.rindex("/")+1
  	item_end = url.rindex(".")
  	url_filename = PWD+url[item_start:item_end]
  	if not os.path.exists(url_filename):
  		os.makedirs(url_filename)
  	text = requestpageText(url)
  	patterns = re.compile(r'第\d张"\ssrc="(.*.jpg)')
  	listp = re.findall(patterns,text)

  	print(url,listp)
  	for x in listp:
  		patterns = re.compile(r'http.*?.jpg')
  		image =re.search(patterns,x,flags=0).group(0)
  		image_start = image.rindex("/")+1
  		image_filename = url_filename+"/"+image[image_start:]
  		if os.path.isfile(image_filename):
  			print("文件存在：",image_filename)
  			continue
  		PhotoName += 1
  		downfile(image_filename,url=image)



PWD = PWD+"qingchun/"
if not os.path.exists(PWD):
  	os.makedirs(PWD)

for x in range(1,3):
  site = "http://www.meizitu.com/a/qingchun_3_%d.html" %x
  text = requestpageText(site)
  patterns = re.compile(r'http:.*?/\d*?.html')
  istp = re.findall(patterns,text)
  for href in istp:#详情页
    getImageDetail(href)

print ("You have down %d photos" %PhotoName)



