import scrapy
import time
from scrapy.selector import Selector

class QuotesSpider(scrapy.Spider):
    name = "amazon2"
    start_urls = [
        'https://www.amazon.com.br/Automatize-Tarefas-Ma%C3%A7antes-com-Python/dp/8575224468/ref=sr_1_1?ie=UTF8&qid=1503414264&sr=8-1&keywords=automatize+tarefas+ma%C3%A7antes+com+python'
    ]

    def parse(self, response):
        for i in range(10):
            #response.css('div.info-produto a::text')[0].extract()
            for produto in  response.css('li.swatchElement'):
                yield  {
                    #'desc':produto.css('span.productTitle::text').extract_first()
                    'preco':produto.css('span.a-size-base::text').re(r'\w*\,\w\w'), 'data':23
                }

                print('aguardando 5 segundos')
                time.sleep(5)

