# -*- coding:gbk -*-
import urllib
import urllib2
import datetime
import MySQLdb

myUrl='http://secondhandhouse.duapp.com/insert.jsp?fundate=%s&num=%s'
startTag='<span id="ess_ctr5112_FDCJY_SignOnlineStatistics_residenceCount4" class="fontfamily">'
endTag="</span>"
def test():
	print "hello,crawl test function"
def insertToDb(dateStr,sellNo):
	con = MySQLdb.connect('10.12.131.124','root','123456','fangchan')
	cur = con.cursor()
	sqlStr = "insert into secondfund values ('%s','%s');" % (dateStr,sellNo)
	log(sqlStr)
	cur.execute(sqlStr);
	return sqlStr;
def getSecondSellNumber(yestStr,html):
	indexS = html.find(startTag);	
	if(indexS!=-1):
		indexE=html.find(endTag,indexS)
		if(indexE!=-1 and indexE>indexS):
			start=indexS+len(startTag)
			sellNumber=html[start:indexE]
			log("%s second fund sell no is %s" % (yestStr,sellNumber))
			return sellNumber

def getYesterdayStr():
	yesterday = datetime.date.today()-datetime.timedelta(1)
	yestStr=yesterday.strftime("%Y%m%d")
	return yestStr
def log(sth):
	nowStr = datetime.datetime.now().strftime("[%Y%m%d %H:%M:%S] ")
	print nowStr+sth
if __name__ == "__main__":
	urlme="http://www.bjjs.gov.cn/tabid/2167/Default.aspx" 
	log("begin crawl "+ urlme)
	req= urllib2.Request(urlme)
	html=urllib2.urlopen(req).read().decode("utf-8").encode("gb18030")
	yestStr=getYesterdayStr()
	filename = "/search/secondfund/data/fund.out."+ yestStr
	f = file(filename,'w')
	log("write file "+ filename)
	f.write(html)
	f.close
	sN = getSecondSellNumber(yestStr,html)
	Sql = insertToDb(yestStr,sN)
	f = file("bakup.sql",'a')
	log("write file backup.sql ")
	f.write(Sql)
	url_final = myUrl % (yestStr,sN);
	print url_final
	try:
		req = urllib2.Request(url_final)
	       	html=urllib2.urlopen(req).read().decode("utf-8").encode("gb18030")
	except Exception,e:
		print e
		print "error"

