import scrapy


class AmazonReviewSpider(scrapy.Spider):
    name = 'amazon_review'
    allowed_domains = ['www.amazon.in']
    start_urls = ['http://www.amazon.in/']

    def parse(self, response):
        pass
