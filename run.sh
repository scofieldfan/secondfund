Date=$(date +"%Y%m%d")
echo "***************$Date begin crawl web **************************************"
cd /search/secondfund
python /search/secondfund/crawl.py 
