#!/bin/bash
rm -rf /usr/src/app/scrappers/nuuvem.json &&
/usr/local/bin/scrapy runspider /usr/src/app/scrappers/nuuvem.py -o /usr/src/app/scrappers/nuuvem.json