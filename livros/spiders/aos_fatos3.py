import scrapy
import time
class AosFatosSpider(scrapy.Spider):
    name = 'aos_fatos3'

    start_urls = ['https://aosfatos.org/noticias/checamos/verdadeiro/?page=1']

    def parse(self, response):
        pass