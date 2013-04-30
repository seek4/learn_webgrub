#!/usr/bin/python
# coding: UTF-8


import urllib

def	cbk(a,b,c):
	"""回调函数
	@a：已经下载好的数据块
	@b：数据块的大小
	@c：远程文件的大小
	"""

	per = 100.0*a*b/c
	if per>100:
		per = 100
	print '%.2f%%'% per


url = "http://www.baidu.com"
local = '/home/outan/learn/baidu.html'
urllib.urlretrieve(url,local,cbk)
