from scrapy.spiders import XMLFeedSpider
from liebertpub.items import LiebertpubItem
from datetime import datetime

class ItemsSpider(XMLFeedSpider):
    name = 'items'
    allowed_domains = ['liebertpub.com']
    start_urls = ['https://www.liebertpub.com/action/showFeed?ui=0&mi=3dss5k&ai=sy&jc=fpd&type=etoc&feed=rss']
    iterator = 'html' # you can change this; see the docs
    itertag = 'item' # change it accordingly

    
    def parse_node(self, response, selector):
        item = LiebertpubItem()
        
        item['title'] = selector.xpath('title/text()').get()
        item['link'] = selector.xpath('url/text()').get()
        item['creator'] = selector.xpath("creator/text()").get()
        date = selector.xpath("date/text()").get()
        item['date'] = datetime.strptime(date,"%Y-%m-%dT%H:%M:%SZ")
        return item

        

