## coding: utf-8

#>>> sel.xpath("//span[@class='a-size-base']//text()").extract()
#sel.xpath("//span[@class='a-color-price']//text()").extract()
import scrapy
import time
from datetime import date

import oauth2
import json
import urllib.parse
from scrapy.selector import Selector
class QuotesSpider(scrapy.Spider):
    name = "amazon4"
    start_urls = [
        'https://www.amazon.com.br/Automatize-Tarefas-Ma%C3%A7antes-com-Python/dp/8575224468/ref=sr_1_1?ie=UTF8&qid=1503414264&sr=8-1&keywords=automatize+tarefas+ma%C3%A7antes+com+python'
    ]

    def parse(self, response):
        sel = Selector(response)

        print('')
        print('##########################################################')
        for i in range(2):
            for produto in sel.xpath("//span[@id='productTitle']//text()").extract():
                print('produto: {}'.format(produto[:50]))
                print('preço: {}'.format(sel.xpath("//span[@class='a-color-price']//text()").extract_first()))
                print('data: {}'.format(date.today()))
            print('##########################################################\n')
            time.sleep(0.9 )


    def comprar(self,preco):
        consusmer_key = ''
        consusmer_secret = ''
        token_key = ''
        token_secret = ''

        consumer = oauth2.Consumer(consusmer_key, consusmer_secret)
        token = oauth2.Token(token_key, token_secret)
        cliente = oauth2.Client(consumer, token)

        pesquisa = 'livro, automatize tarefas maçantes com python, preço: R$' + str(preco)
        pesquisa_codificada = urllib.parse.quote(pesquisa, safe='')

        requisicao = cliente.request('https://api.twitter.com/1.1/statuses/update.json?status=' + pesquisa_codificada,
                                     method='POST')
        decodificar = requisicao[1].decode()

        objeto = json.loads(decodificar)

        print(objeto)
