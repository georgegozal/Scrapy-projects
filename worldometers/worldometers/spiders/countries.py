import scrapy
import logging

class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        #title = response.xpath('//h1/text()').get()
        countries = response.css('td a')
        #countries = response.xpath('//td/a')

        for country in countries:
            #name = country.xpath('.//text()').get()#we start with "." after response , on variable 
            name = country.css('::text').get()
            link = country.xpath('.//@href').get()
            #link = country.css('::attr(href)').get()

            url = response.urljoin(link)
            #url = f"https://www.worldometers.info{link}"

            yield response.follow(url=link, callback=self.parse_country, meta={'country_name':name}) # meta={} ასე შეგვიძლია გამოვიტანოთ ცვლადის მნიშვნელობა ლექსიკონით
            #yield scrapy.Request(url=url)


    def parse_country(self,response):
        name = response.request.meta['country_name']  # ასე შეგვიძლია მივიღოთ წინა მეთოდიდან გამოგზავნილი meta თი key ს სახელით
        #logging.info(response.url)
        rows = response.xpath("(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr")
        for row in rows:
            year       = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()
            world_population = row.xpath(".//td[12]/text()").get()
            yield {
                'country_name':name,
                'year':year,
                'population':population,
                'world_population':world_population
            }