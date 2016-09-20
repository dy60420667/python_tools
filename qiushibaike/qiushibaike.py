import requests
import re

class qiushibaike:
  	def __init__(self):
  		self.head = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
  		self.TimeOut = 30
  		self.url = "http://www.qiushibaike.com/8hr/page/%d"
  		self.page = 1

  	def requestpageText(self,url):
  		try:
  			print("开始获取数据:",url)
  			Page = requests.session().get(url,headers=self.head,timeout=self.TimeOut)
  			Page.encoding = "utf-8"
  			return Page.text
  		except BaseException as e:
  			print("联网失败了...",e)

  	def downurl(self,page):
  		url = self.url%(page)
  		text = self.requestpageText(url)
  		patterns = re.compile(r'<div class="article block untagged mb15".*?title="(.*?)">.*?<div class="content">(.*?)</div>.*?<i class="number">(.*?)</i> 好笑.*?<i class="number">(.*?)</i> 评论',re.S)
  		items = re.findall(patterns,text)
  		index = 0
  		while  index < len(items):
  			try:
	  			x = items[index]
	  			print("作者：{0}   好笑：{1}   评论{2}".format(x[0],x[2],x[3]))
	  			print(x[1])
	  			
	  			text = input("按回车键进入下一项")
	  			print()
	  			print()	
  			except Exception as e:
  				print(e)
  			index+=1
  			
  		self.page +=1
  		self.downurl(self.page)

  	def start(self):
  		self.downurl(self.page)
  		



q = qiushibaike()
text = q.start()
