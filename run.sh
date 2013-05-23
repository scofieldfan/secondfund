Date=$(date +"%Y%m%d")
echo "***************$Date begin crawl web **************************************"
cd /search/secondfund
git add data/*
python /search/secondfund/crawl.py 
git commit -a -m "$Date add crawl data" 
git push -u origin master 
