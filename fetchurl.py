# -*- coding:gbk -*-
import urllib
import urllib2
import datetime
import MySQLdb

urlme="http://www.newsmth.net/nForum/#!board/ITExpress"
def log(sth):
	nowStr = datetime.datetime.now().strftime("[%Y%m%d %H:%M:%S] ")
	print nowStr+sth
if __name__ == "__main__":
	log("begin crawl "+ urlme)
	req= urllib2.Request(urlme)
	html=urllib2.urlopen(req).read().decode("utf-8").encode("gb18030")
	print html
