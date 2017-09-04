import scrapy
import re

class QuotesSpider(scrapy.Spider):
    name = "redbug_preco_re"
    start_urls = [
        'https://www.redbug.com.br/camisetas-masc',
        'https://www.redbug.com.br/camisetas-masc?pagina=2',
        'https://www.redbug.com.br/camisetas-masc?pagina=3',
        'https://www.redbug.com.br/camisetas-masc?pagina=4',
        'https://www.redbug.com.br/camisetas-masc?pagina=3'

    ]

    def parse(self, response):
        #response.css('div.info-produto a::text')[0].extract()
        for produto in response.css('div.listagem-item'):
            yield {
                'desc':produto.css('a::text').extract_first(),
                'preco': produto.css('strong.preco-venda::text').re(r'\w*\,\w\w'),
                'url': response.css('div.listagem-item a').extract_first()
            }
            descr = produto.css('a::text').extract_first(),
            preco = produto.css('strong.preco-venda::text').re(r'\w*\,\w\w')
            url = response.css('div.listagem-item a').extract_first()
            print(descr, preco, url)