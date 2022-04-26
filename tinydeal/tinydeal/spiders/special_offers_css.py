import scrapy


class SpecialOffersCssSpider(scrapy.Spider):
    name = 'special_offers_css'
    allowed_domains = ['web.archive.org/']
    start_urls = ['https://web.archive.org/web/20190225123327/https://www.tinydeal.com/specials.html']

    def parse(self, response):
        
        for row in response.css('ul.productlisting-ul div.p_box_wrapper li'):
            yield {
                'title' :row.css('a.p_box_title::text').get(),
                'url'   :response.urljoin(row.css('a.p_box_title::attr(href)').get()),
                'discounted_price':row.css('div.p_box_price span.productSpecialPrice.fl::text').get(),
                'original_price'  :row.css('div.p_box_price span.normalprice.fl::text').get()
                #'User-Agent':response.request.headers['User-Agent']
            }

        next_page = response.css("a.nextPage::attr(href)").get()

        if next_page:
            scrapy.Request(url=next_page, callback=self.parse)