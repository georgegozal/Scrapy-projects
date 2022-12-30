import scrapy
from scrapy_splash import SplashRequest


class DgftGovSpider(scrapy.Spider):
    name = 'dgft_gov'
    allowed_domains = ['www.dgft.gov.in']

    script = """
    function main(splash,args)
        splash:on_request(function(request)
            request:set_header(
                'User-Agent'," Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
                'accept', 'text/html, */*; q=0.01',
 		        'accept-encoding', 'gzip, deflate, br',
 			    'accept-language', 'en-US,en;q=0.9,ka;q=0.8,es;q=0.7',
 			    'content-type', 'application/x-www-form-urlencoded; charset=UTF-8',
 			    'origin', 'https://www.dgft.gov.in',
 			    'referer', 'https://www.dgft.gov.in/CP/?opt=itchs-import-export',
 			    'sec-ch-ua', '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
 			    'sec-ch-ua-mobile', '?0',
 			    'sec-ch-ua-platform', '"Linux"',
 			    'sec-fetch-dest', 'empty',
 			    'sec-fetch-mode', 'cors',
 			    'sec-fetch-site', 'same-origin',
 			    'sec-gpc', '1')
        end)
        splash.private_mode_enabled = false
        url = args.url
        assert(splash:go(url))
        assert(splash:wait(2))

	    menu_item = assert(splash:select_all("div.row > div > div > a"))
        menu_item[1]:mouse_click()
        assert(splash:wait(3))
        splash:set_viewport_full()
        return splash:html()
    end""" 

    def start_requests(self):
        
        yield SplashRequest(
            url="https://www.dgft.gov.in/CP/?opt=itchs-import-export",
            callback=self.parse,
            endpoint="execute",
            args={'lua_source':self.script}
        )


    def parse(self, response):
        for item in response.xpath("//tbody/tr"):
            title = item.xpath("./td[2]/text()").get()
            # pdf_link = response.urljoin(
            #     item.xpath("./td[4]/a/@href")
            # )
            pdf = item.xpath("./td[4]/a/@href").get()
            
            yield {
                'Title':title,
                'pdf':[pdf],
                
            }
