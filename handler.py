# _*_ coding:gbk _*_
import os 
import crawl
list =  os.listdir("./data")
crawl.test()
for f in list:
	 fl = file("./data/"+f);
	 crawl.log("handler the file %s " % f)
	 html=fl.read()
         yesStr=f.replace("fund.out.","")
	 crawl.log(yesStr)
	 #yesStr = crawl.getYesterdayStr()
	 sn = crawl.getSecondSellNumber(yesStr,html)
       	 crawl.insertToDb(yesStr,sn)
	 
