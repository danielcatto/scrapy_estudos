import scrapy
import re


class QuotesSpider(scrapy.Spider):
    name = "amazon1"
    start_urls = [
        'https://www.amazon.com.br/Automatize-Tarefas-Ma%C3%A7antes-com-Python/dp/8575224468/ref=sr_1_1?ie=UTF8&qid=1503414264&sr=8-1&keywords=automatize+tarefas+ma%C3%A7antes+com+python'
    ]

    def parse(self, response):
        #response.css('div.info-produto a::text')[0].extract()
        for produto in  response.css('li.swatchElement'):
            yield {
                #'desc':produto.css('span.productTitle::text').extract_first()
                'preco':produto.css('span.a-size-base::text').re(r'\w*\,\w\w'),'dia':'hoje'
            }


