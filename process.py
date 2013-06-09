# -*- coding:gbk -*-
import urllib
import urllib2
import datetime

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
	f.close()

def log(sth):
	nowStr = datetime.datetime.now().strftime("[%Y%m%d %H:%M:%S] ")
	print nowStr+sth
if __name__ == "__main__":
    f = open("filterPredict.out")
    lines = f.readlines()
    simpleList = []
    for line in lines:
        if line.find("行情")!=-1 :
            simpleList.append(line)
            log(line)
    f.close()
    simpleList.sort()
    writeFile("hangqing.out",''.join(simpleList))
