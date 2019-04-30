import scrapy
import configparser
from NikkeiScrapy.items import NikkeiItem
import datetime

class NikkeiSpider(scrapy.Spider):
    # Your spider definition
    # config = configparser.ConfigParser()
    # config.read('PyConfig.ini')
    name = "Nikkei_Spider"
    # allowed_domains = [config.get('Nikkei', 'Domain')]
    # start_urls = [config.get('Nikkei', 'SearchUrl')+'貿易']
    config = configparser.ConfigParser()
    config.read('PyConfig.ini')
    allowed_domains = [config.get('Nikkei', 'Domain')]
    start_urls = [config.get('Nikkei', 'LoginUrl')]
    # start_urls = ['https://r.nikkei.com/search?keyword=貿易']


    def parse(self, response):
        # for article in response.css('div.stream-layout__card search__result-item-content nui-layout__item nui-card--no-image'):
        # for article in response.css('div.nui-card__container'):
        #     item = NikkeiItem()
        #     item['title'] = article.css('h3.nui-card__title a::text').extract()
        #     # item['title'] = map(lambda str:str.strip(), item['title'])
        #
        #     item['detail'] = article.css('div.nui-card__sub-text a::text').extract()
        #     # item['detail'] = self.rmblank(item['detail'])
        #     # print(item['title'])
        #
        #     item['insert_datetime'] = datetime.datetime.today()
        #     yield item
        return scrapy.FormRequest.from_response(
            response,
            formdata={'username': 'se.nikix@outlook.jp', 'password': 'Neosigh27'},
            callback=self.parse_articlelist
        )
        # for href in response.css('div.nui-card__container a::attr(href)'):
        #     url_sub = response.urljoin(href.extract())
        #     yield scrapy.Request(url_sub, callback=self.parse_article)

    def parse_articlelist(self,response):
        # for article in response.css('div.nui-card__container'):




        # item['title'] = article.css('h3.nui-card__title a::text').extract()
        # item['title'] = article.css('cmnc-middle JSID_key_fonthln m-streamer_medium')

        # item['detail'] = article.css('div.nui-card__sub-text a::text').extract()


        # next_page = response.xpath('/html/body/div[3]/main/div/div[5]/div/div[2]/button')
        # if next_page:
        #     url = response.urljoin(next_page[0].extract())
        #     yield scrapy.Request(url, callback=self.parse)
        return scrapy.Request(self.config.get('Nikkei', 'SearchUrl')+'貿易', callback=self.parse_article)
        # else:
        #     return
        # pass

    def parse_article(self,response):
        item = NikkeiItem()
        item['I1_title'] = response.css('span.cmnc-middle JSID_key_fonthln m-streamer_medium::text').extract()
        articles = response.css('div.cmn-article_text a-cf JSID_key_fonttxt m-streamer_medium')
        item['I2_detail'] = articles.css('p::text').extract()
        item['I3_insert_datetime'] = datetime.datetime.today()
        yield item
    # process = CrawlerProcess({
    # 'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    # })

# process.crawl(MySpider)
# process.start() # the script will block here until the crawling is finished

