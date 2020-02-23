import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
import time
class AosFatosSpider(scrapy.Spider):
    name = 'investigamos'

    start_urls = ['https://aosfatos.org/noticias/investigamos/?page=1']

    def parse(self, response):
        sel = Selector(response)
        links = sel.xpath("//section[@id='three-cards']/a/@href").getall()

        for link in links:
            print('links::::::', link)
            yield Request(response.urljoin(link), callback=self.parse_noticia)

        next_page = sel.xpath("//div[@class='pagination']//a/@href").getall()

        for i in range(len(sel.xpath("//div[@class='pagination']//a/@href").getall())):
            yield Request(response.urljoin(next_page[i]))

    def parse_noticia(self, response):

        autor = response.xpath("//article//p[@class='author']/text()").get()
        data = ' '.join(response.xpath("//article//p[@class='publish_date']/text()").get().split())
        titulo = response.xpath("//article/h1/text()").get()
        url = response.url
        quotes = response.xpath("//article/blockquote/p")
        for quote in quotes:
            quotes_text = quote.xpath('.//text()').get()
            status = quote.xpath('./parent::blockquote/preceding-sibling::figure//figcaption/text()').get()
            if status is None:
                status = 'nao recuperado'

            yield {
                'autor': autor,
                'data': data,
                'titulo': titulo,
                'url': url,
                'quote': quotes_text,
                'status': status
            }
