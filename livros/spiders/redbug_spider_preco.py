import scrapy
import re

class QuotesSpider(scrapy.Spider):
    name = "redbug_preco"
    start_urls = [
        'https://www.redbug.com.br/camisetas-masc'
    ]

    def parse(self, response):
        #response.css('div.info-produto a::text')[0].extract()
        for produto in response.css('div.info-produto'):
            yield {
                'desc':produto.css('a::text').extract_first(),
                'preco': produto.css('strong.preco-venda::text').extract_first(),
                'preco':produto.css('strong.preco-venda::text').extract_first()
            }

