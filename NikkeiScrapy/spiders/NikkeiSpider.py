import scrapy
import configparser
from NikkeiScrapy.items import NikkeiItem


class NikkeiSpider(scrapy.Spider):
    # Your spider definition
    # config = configparser.ConfigParser()
    # config.read('PyConfig.ini')
    name = "Nikkei_Spider"
    # allowed_domains = [config.get('Nikkei', 'Domain')]
    # start_urls = [config.get('Nikkei', 'SearchUrl')+'貿易']
    allowed_domains = ['r.nikkei.com']
    start_urls = ['https://r.nikkei.com/search?keyword=貿易']

    def rmblank(str):
        return str.strip()

    def parse(self, response):
        # for article in response.css('div.stream-layout__card search__result-item-content nui-layout__item nui-card--no-image'):
        for article in response.css('div.nui-card__container'):
            item = NikkeiItem()
            item['title'] = map(self.rmblank(), article.css('h3.nui-card__title a::text').extract())
            # item['title'] = map(lambda str:str.strip(), item['title'])

            item['detail'] = article.css('div.nui-card__sub-text a::text').extract()
            # item['detail'] = self.rmblank(item['detail'])
            # print(item['title'])
            yield item

        # next_page = response.css('button.nui-button search__more-button')
        next_page = response.xpath('/html/body/div[3]/main/div/div[5]/div/div[2]/button')
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, callback=self.parse)

        print item['title']
        # else:
        #     return
        # pass
    # process = CrawlerProcess({
    # 'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    # })


# process.crawl(MySpider)
# process.start() # the script will block here until the crawling is finished

