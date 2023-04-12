
import urllib
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import os
import time

######################## 子函数部分 #########################
def getImg(url, localpath):
	htmlfile = open(url, 'rb')			#以只读的方式打开本地html文件
	htmlpage = htmlfile.read()
	soup = BeautifulSoup(htmlpage, "html.parser")	#实例化一个BeautifulSoup对象
	img_content=soup.select('img')
	for i in img_content:
		url_end = i['src']
		img_url = 'file:///'+localPath + url_end[2:100]	#从html中读取对应的图片名称
	img_name = folder_path + '/' + str(index) +'.jpg'	#生成新的图片名字，以123数字排序
	urlretrieve(img_url, img_name)			#下载(复制)该图片到目标文件夹
	print('%d.jpg' %(index))	#显示下载
	#time.sleep(0.01)		#自定义延时 0.01s
	htmlfile.close()

def getcover():	#获取封面
	cover_name = folder_path + '/0.jpg'
	cover_jpg = 'file:///'+ localPath + '/image/cover.jpg'
	cover_png = 'file:///'+ localPath + '/image/cover.png'
	if(os.path.exists(cover_png)):
		cover_url = cover_png
		urlretrieve(cover_url, cover_name)
	if(os.path.exists(cover_jpg)):
		cover_url = cover_jpg
		urlretrieve(cover_url, cover_name)
	print('0.jpg 封面')

########################### 主程序 ###########################
######## 请事先将批量解压好的zip文件夹以123数字重命名 ########

filepath = os.getcwd()	#获取当前目录
chp = 1			#初始章节
localPath = filepath + '/' + str(chp)	#获取初始章节文件夹目录

while(os.path.exists(localPath)):			#判断章节是否存在
	localPath = filepath + '/' + str(chp)	#批量获取章节文件夹目录
	folder_path = filepath + '/pics/' + str(chp)#生成用于储存结果图片的pics文件夹目录
	os.makedirs(folder_path, exist_ok=True)	#创建pics文件夹

	index = 1
	url = localPath + '/html/' + str(index) + '.html'#初始生成html文件目录
	getcover()#子函数获取封面
	while(os.path.exists(url)):
			getImg(url, localPath)	#调用子函数获取余下图片
			index = index + 1
			url = localPath + '/html/' + str(index) + '.html'#批量生成html文件目录
	print('================= 第%d章处理完成 ==================' %(chp))
	chp = chp + 1
	localPath = filepath + '/' + str(chp)	#章节文件夹目录+1
print('===================== 全部处理完成 ====================')
print()
input('按回车退出')
sys.exit(0)
