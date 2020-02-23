import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
import time
import re

class AosFatosSpider(scrapy.Spider):
    name = 'aos_fatos2-teste'

    start_urls = ['https://aosfatos.org/noticias/checamos/verdadeiro/?page=1']

    def parse(self, response):
        sel = Selector(response)
        links = sel.xpath("//section[@id='three-cards']/a/@href").getall()

        for link in links:
            yield Request(response.urljoin(link), callback=self.parse_noticia)

        next_page = sel.xpath("//div[@class='pagination']//a/@href").getall()

        for i in range(len(sel.xpath("//div[@class='pagination']//a/@href").getall())):
            yield Request(response.urljoin(next_page[i]), callback=self.parse)


    def parse_noticia(self, response):
       
        autor = response.xpath("//article//p[@class='author']/text()").get()
        if autor is None:
            autor = 'autor: dados não recuperado'

        data = ' '.join(response.xpath("//article//p[@class='publish_date']/text()").get().split())
        titulo = response.xpath("//article/h1/text()").get()
        if titulo == '\n          ':
            titulo = 'titulo N naõ recuperado'
        url = response.url
        quotes = response.xpath("//article/blockquote/p")

        for quote in quotes:
            quotes_text = quote.xpath('.//text()').get()
            status = quote.xpath('./parent::blockquote/preceding-sibling::figure//figcaption/text()').get()
            if status is None:
                status = 'nao recuperado'
            data_pub = self.to_date(data)

            #print(autor, titulo, quotes_text, data_pub, url, status,'\n\n---------\n\n\n\')
            print('''
                autor: {}
                titulo: {}
                quotes: {}
                data publicação: {}
                url: {}
                status: {}
            '''.format(autor, titulo, quotes_text, data_pub, url, status))
        
        time.sleep(.3)



    def to_date(self, data):

        dia = re.findall(r'\d+', data)
        mes = re.findall(r'\w\w+[a-z]+', data)
        ano = re.findall(r'\d\d\d+', data)
        dia_str = dia[0]
        ano_str = ano[0]

        if (mes[0] == 'janeiro'):
            mes_str = '1'
        if (mes[0] == 'fevereiro'):
            mes_str = '2'
        if (mes[0] == 'março'):
            mes_str = '0'
        if (mes[0] == 'abril'):
            mes_str = '4'
        if (mes[0] == 'maio'):
            mes_str = '5'
        if (mes[0] == 'junho'):
            mes_str = '6'
        if (mes[0] == 'julho'):
            mes_str = '7'
        if (mes[0] == 'agosto'):
            mes_str = '8'
        if (mes[0] == 'setembro'):
            mes_str = '9'
        if (mes[0] == 'outubro'):
            mes_str = '10'
        if (mes[0] == 'novembro'):
            mes_str = '11'
        if (mes[0] == 'dezembro'):
            mes_str = '12'
        if (mes[0] == '0'):
            mes_str == '1'

        data_pub = ano_str +'-'+ mes_str + '-' + dia_str
        return data_pub




'''
    def parseNoticia(self, response):
        yield {
            'titulo' : response.xpath("//article/h1/text()").get(),
            'texto': response.xpath("//article/p/text()").get(),
            'status': response.xpath("//article/figure/figcaption//text()").get(),
            'url': response.url
            }



'''