git add data/*
Date=$(date +"%Y%m%d")
python crawl.py
git commit -m "$Date add crawl data"
git push -u origin master
