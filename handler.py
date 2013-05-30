# _*_ coding:gbk _*_
import os 
import crawl
import urllib2
list =  os.listdir("./data")
crawl.test()
myUrl='http://secondhandhouse.duapp.com/insert.jsp?fundate=%s&num=%s'
for f in list:
	 fl = file("./data/"+f);
	 crawl.log("handler the file %s " % f)
	 html=fl.read()
         yesStr=f.replace("fund.out.","")
	 crawl.log(yesStr)
	 #yesStr = crawl.getYesterdayStr()
	 sn = crawl.getSecondSellNumber(yesStr,html)
         url_final = myUrl % (yesStr,sn);
	 print url_final
	 try:
		req = urllib2.Request(url_final)
	       	html=urllib2.urlopen(req).read().decode("utf-8").encode("gb18030")
	 except:
		print "error"
       	 crawl.insertToDb(yesStr,sn)
	 
