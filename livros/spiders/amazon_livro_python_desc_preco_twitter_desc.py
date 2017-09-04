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
    name = "amazonTwitter"
    start_urls = [
        'https://www.amazon.com.br/Automatize-Tarefas-Ma%C3%A7antes-com-Python/dp/8575224468/ref=sr_1_1?ie=UTF8&qid=1503414264&sr=8-1&keywords=automatize+tarefas+ma%C3%A7antes+com+python',
        'https://www.amazon.com.br/Introdu%C3%A7%C3%A3o-%C3%A0-Programa%C3%A7%C3%A3o-com-Python/dp/8575224085/ref=pd_sim_14_3?_encoding=UTF8&psc=1&refRID=A27DQPZMEM90Y1GKJZ0N',
        'https://www.amazon.com.br/Curso-Intensivo-Python-Eric-Matthes/dp/8575225030/ref=pd_sim_14_3?_encoding=UTF8&psc=1&refRID=10GDJK1QJ6DCTKN7T76E'

    ]

    def parse(self, response):
        sel = Selector(response)
        print('')
        print('##########################################################')
        for produto in sel.xpath("//span[@id='productTitle']//text()").extract():
            yield
            print('\n\nproduto: {}'.format(produto[:50]))
            print('preço: {}'.format(sel.xpath("//span[@class='a-color-base']//text()").re(r'\w\w\,\w\w')[0]))
            print('data: {}'.format(date.today()))
        print('##########################################################\n')


    def comprar(self,preco):
        consusmer_key = 'yT57HTvtM7drPqQ1fVMtbdsGJ'
        consusmer_secret = 'AYke23tMy9QNMuWpVMD8UTu7MiP8VL2Aee0j7KT8HuEV88uSqZ'
        token_key = '50165680-o7CcGmvB9XmSEdDkWGNNnjUEUNsBXD4vErRMG22k1'
        token_secret = 'zRuIUYEuJfiV7pXQPWkzYgy1a5KODWseIGSoC7iGHJGkU'

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