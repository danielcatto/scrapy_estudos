import scrapy
import time
from datetime import date

import oauth2
import json
import urllib.parse

class QuotesSpider(scrapy.Spider):
    name = "amazon3"
    start_urls = [
        'https://www.amazon.com.br/Automatize-Tarefas-Ma%C3%A7antes-com-Python/dp/8575224468/ref=sr_1_1?ie=UTF8&qid=1503414264&sr=8-1&keywords=automatize+tarefas+ma%C3%A7antes+com+python'
    ]

    def parse(self, response):
        print('\n\n\n')
        print("############ SAIDA DO CLIENTE#############")
        while True:
            for produto in  response.css('li.swatchElement'):
                yield{
                    #'desc':produto.css('span.productTitle::text').extract_first()
                    'preco':produto.css('span.a-size-base::text').re(r'\w*\,\w\w'), 'data':date.today()
                }
                #'desc':produto.css('span.productTitle::text').extract_first()
                valor = produto.css('span.a-size-base::text').re(r'\w*\,\w\w')[0]
                preco = float(valor.replace(",", "."))
                data = date.today()
                if preco <= 57:
                    self.twittar(preco)
                    print("\n############# FIM ##################\n\n\n")
                    return 0
                print('aguardando 30 segundos')
                time.sleep(60)

        print('saida do cliente\nvalor: {}\ndata: {}'.format(preco, data))
        print('')
        print("############# FIM ##################")
        print('\n\n\n')

    def twittar(self,preco):
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