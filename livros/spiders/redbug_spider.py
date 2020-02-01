'''
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }
'''
import scrapy
class QuotesSpider(scrapy.Spider):
    name = "redbug"
    start_urls = [
        'https://www.redbug.com.br/camisetas-masc'
    ]

    def parse(self, response):
        #response.css('div.info-produto a::text')[0].extract()
        for produto in response.css('div.info-produto'):
            yield {
                #'desc': quote.css('span.text::text').extract_first(),
                'desc':produto.css('a').extract()
            }

