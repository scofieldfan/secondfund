# -*- coding:gbk -*-
import urllib
import urllib2
import datetime
import MySQLdb

myUrl='http://www.zhujiage.com.cn/Article/showlist.php?tid=24&TotalResult=38533&PageNo=%s'
def test():
	print "hello,crawl test function"
def insertToDb(dateStr,sellNo):
	con = MySQLdb.connect('10.12.131.124','root','123456','fangchan')
	cur = con.cursor()
	sqlStr = "insert into secondfund values ('%s','%s');" % (dateStr,sellNo)
	log(sqlStr)
	cur.execute(sqlStr);
	return sqlStr;

def getSecondSellNumber(html):
	indexS = html.find(startTag);	
	if(indexS!=-1):
		indexE=html.find(endTag,indexS)
		if(indexE!=-1 and indexE>indexS):
			start=indexS+len(startTag)
			sellNumber=html[start:indexE]
			log("%s second fund sell no is %s" % (yestStr,sellNumber))
			return sellNumber
def writeFile(filename)
	f = file(filename,'w')
	log("write file "+ filename)
	f.write(html)
	f.close

def getYesterdayStr():
	yesterday = datetime.date.today()-datetime.timedelta(1)
	yestStr=yesterday.strftime("%Y%m%d")
	return yestStr
def log(sth):
	nowStr = datetime.datetime.now().strftime("[%Y%m%d %H:%M:%S] ")
	print nowStr+sth
if __name__ == "__main__":
	simpleList=[]
	for i in range(1,10):
		url = myUrl % i
		log("begin crawl "+ url)
		req= urllib2.Request(url)
		html=urllib2.urlopen(req).read()
		
