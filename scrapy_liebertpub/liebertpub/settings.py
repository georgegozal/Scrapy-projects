BOT_NAME = 'liebertpub'

SPIDER_MODULES = ['liebertpub.spiders']
NEWSPIDER_MODULE = 'liebertpub.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32



COOKIES_ENABLED = False


DEFAULT_REQUEST_HEADERS = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.9,ka;q=0.8,es;q=0.7",
    "User-Agent":USER_AGENT,
    "Cache-Control":"max-age=0",
    "Connection":"keep-alive",
    "Host":"www.liebertpub.com",
    "If-Modified-Since":"Fri, 06 May 2022 03:03:05 GMT",
    "sec-ch-ua":' Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":'"Linux"',
    "Sec-Fetch-Dest":"document",
    "Sec-Fetch-Mode":"navigate",
    "Sec-Fetch-Site":"none",
    "Sec-Fetch-User":"?1",
    "sec-gpc":"1",
    "Upgrade-Insecure-Requests":"1"    
}

CONCURRENT_REQUESTS = 1
DOWNLOAD_DELAY = 5
AUTOTHROTTLE_MAX_DELAY = 3
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5
