import scrapy
import time
class AosFatosSpider(scrapy.Spider):
    name = 'aos_fatos2'

    start_urls = ['https://aosfatos.org/noticias/checamos/verdadeiro/?page=1']

    def parse(self, response):
        links = response.xpath("//section[@id='three-cards']/a/@href").getall()
        pages_url = response.xpath("//div[@class='pagination']/a/@href").getall()

        for link in links:
            yield scrapy.Request(response.urljoin(link), callback=self.parseNoticia)

        for url in pages_url:
            print('\n\n\n\n\n', response.urljoin(url), '\n\n\n\n\n\n\n')
            yield scrapy.Request(response.urljoin(url), callback=self.parseNoticia)



    def parseNoticia(self, response):
        yield {
            'titulo' : response.xpath("//article/h1/text()").get(),
            'texto': response.xpath("//article/p/text()").get(),
            'status': response.xpath("//article/figure/figcaption//text()").get(),
            'url': response.url
            }



