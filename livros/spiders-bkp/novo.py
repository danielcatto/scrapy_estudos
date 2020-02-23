## coding: utf-8

import scrapy
from scrapy.selector import Selector

import time
from datetime import date
from facepy import GraphAPI
import oauth2
import json


class QuotesSpider(scrapy.Spider):
    name = "novo"
    start_urls = [
        'https://www.amazon.com.br/Automatize-Tarefas-Ma%C3%A7antes-com-Python/dp/8575224468/ref=sr_1_1?ie=UTF8&qid=1503414264&sr=8-1&keywords=automatize+tarefas+ma%C3%A7antes+com+python'
    ]


    def parse(self, response):
        controle = True
        sel = Selector(response)
        preco_comparativo = 79  #self.para_float(self.para_converte(sel.xpath("//span[@class='a-color-base']//text()").re(r'\w\w\,\w\w')[0]))
        print("\n\n###################################################")
        print('inicio')
        for i in range(3):
            for produto in sel.xpath("//span[@id='productTitle']//text()").extract():
                preco = sel.xpath("//span[@class='a-color-base']//text()").re(r'\w\w\,\w\w')[0]
                data = date.today()
                url = response.url

                yield{
                    'produto': produto, 'preco': preco, 'data': str(data), 'url': url
                }
                time.sleep(10)

            print("\n###################################################\n\n")
            time.sleep(10)