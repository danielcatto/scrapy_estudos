import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
import time
import re
import mysql.connector

class AosFatosSpider(scrapy.Spider):

    name = 'ps2'

    start_urls = ['http://www.portalroms.ch/isos/ps2']

    def parse(self, response):
        links = response.css('span.field-content a::attr(href)').getall()

        for link in links:
            yield Request(response.urljoin(link), callback=self.parse_torrent)

        next_page = response.css('li.pager-next a::attr(href)').get()
        yield Request(response.urljoin(next_page))

    def parse_torrent(self, response):
        titulo = response.css('div#main h1::Text').get()
        data_lancamento = response.css('span.date-display-single::text').get()



        yield {
            'titulo': titulo,
            'data_lancamento': data_lancamento

        }