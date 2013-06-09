# -*- coding:gbk -*-
import urllib
import urllib2
import datetime

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

def getSubString(html,startTag,endTag):
	indexS = html.find(startTag);	
	if(indexS!=-1):
		indexE=html.find(endTag,indexS)
		if(indexE!=-1 and indexE>indexS):
			start=indexS+len(startTag)
			result=html[start:indexE]
			return result
def getSubStringList(html,startTag,endTag):
	result=[];
	indexS = html.find(startTag);	
	while(indexS!=-1):
		indexE=html.find(endTag,indexS)
		if(indexE!=-1 and indexE>indexS):
			start=indexS
			end=indexE+len(endTag)
			tagResult = html[start:end]
			result.append(tagResult)
			indexS = html.find(startTag,indexE);
	return result;
def writeFile(filename,content):
	f = file(filename,'a')
	log("write file "+ filename)
	f.write(''.join(content))
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
	for i in range(1,714):
		url = myUrl % i
		log("begin crawl "+ url)
		req= urllib2.Request(url)
		html=urllib2.urlopen(req).read()
		listHtml =  getSubString(html,'<div class="lmlist">','<div class="showpage">');
		resultList= getSubStringList(listHtml,'<A','</A>')
		for re in resultList:
			if re.find('山东')!=-1:
				log(re)
				simpleList.append(re+"\n")
		writeFile("山东PigPrice.out",simpleList)
		

		
