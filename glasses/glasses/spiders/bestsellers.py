# -*- coding: utf-8 -*-
#from typing_extensions import runtime
import scrapy
#from scrapy.shell import inspect_response


class BestsellersSpider(scrapy.Spider):
    name = 'bestsellers'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers']


    def parse(self, response):
        #inspect_response(response,self) #excecutes scrapy shell for this code # request.headers
        
        for glass in response.xpath("//div[@id='product-lists']/div"):
            yield {
                'name'     :glass.xpath("normalize-space(.//div[@class='p-title']/a/text())").get(),
                #'name'           :str(row.xpath(".//div[@class='p-title']/a/text()").get()).replace('\n','').strip(),
                'url'      :glass.xpath(".//div[@class='product-img-outer']/a/@href").get(),
                'img_url'  :glass.xpath(".//div[@class='product-img-outer'][1]/a/img[@class='lazy d-block w-100 product-img-default']/@data-src").extract_first(),
                'price'    :glass.xpath(".//div[@class='p-price']/div/span/text()").get()

            }

        next_page = response.xpath(
            "//ul[@class='pagination']/li[position() = last()]/a/@href").get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)


        