import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['web.archive.org/']
    #start_urls = ['https://web.archive.org/web/20190225123327/https://www.tinydeal.com/specials.html']
    url = 'https://web.archive.org/web/20190225123327/https://www.tinydeal.com/specials.html'

    def start_requests(self):
        yield scrapy.Request(url=self.url, callback=self.parse, headers={
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
        })

    def parse(self, response):
        for row in response.xpath('//ul[@class="productlisting-ul"]/div/li'):
            yield {
                'title' :row.xpath('.//a[2]/text()').get(),
                'url'   :response.urljoin(row.xpath('.//a[2]/@href').get()),
                'discounted_price':row.xpath('.//div[@class="p_box_price"]/span[1]/text()').get(),
                'original_price'  :row.xpath('.//div[@class="p_box_price"]/span[2]/text()').get(),
                'User-Agent':response.request.headers['User-Agent']
            }

        #next_page = response.xpath('//div[@class="wh_fanye"]/div/div/a[6]/@href').get()   
        next_page = response.xpath('//a[@class="nextPage"]/@href').get()

        if next_page:
            yield scrapy.Request(url=next_page,callback=self.parse, headers={
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
        })