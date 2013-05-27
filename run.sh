Date=$(date +"%Y%m%d")
echo "***************$Date begin crawl web **************************************"
cd /search/secondfund
python /search/secondfund/crawl.py 
git add data/*
git commit -a -m "$Date add crawl data" 
git push -u origin master 
