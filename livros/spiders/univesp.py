## coding: utf-8

import scrapy
import time
from datetime import date

import oauth2
import json
from scrapy.selector import Selector

class QuotesSpider(scrapy.Spider):
    name = "amazonAutomatize"
    start_urls = [
        'https://univesp.br/cursos/engenharia-de-computacao'
    ]


    def parse(self, response):
        controle = True
        sel = Selector(response)
        print("\n\n###################################################")
        for i in range(1):
            for inscricao in sel.xpath("//a[@class='btn']//text()").extract():
                yield{
                    'inscr': inscricao
                }
                time.sleep(3)

