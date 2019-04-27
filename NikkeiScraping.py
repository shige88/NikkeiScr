from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from NikkeiScrapy.spiders.NikkeiSpider import NikkeiSpider


if __name__ == '__main__':
    # spider = NikkeiSpider()
    setting = get_project_settings()
    setting.set('FEED_URI', 'NikkeiOutput.csv')

    # process = CrawlerProcess(setting)
    process = CrawlerProcess(setting)
    process.crawl(NikkeiSpider)
    process.start()