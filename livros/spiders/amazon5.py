import scrapy
import time
from datetime import date

import oauth2
import json
import urllib.parse


class QuotesSpider(scrapy.Spider):
    name = "amazon5"
    start_urls = [
        'https://www.amazon.com.br/Web-Scraping-Python-Ryan-Mitchell/dp/8575224476/ref=sr_1_9?s=books&ie=UTF8&qid=1503538574&sr=1-9&keywords=python'
    ]

    def parse(self, response):
        print('\n\n\n')
        print("############ SAIDA DO CLIENTE#############")
        for i in range(3):
            for produto in  response.css('li.swatchElement'):
                yield{
                    'preco':produto.css('span.a-size-base::text').re(r'\w*\,\w\w'), 'data':date.today()
                }

                valor = produto.css('span.a-size-base::text').re(r'\w*\,\w\w')[0]
                preco = float(valor.replace(",", "."))
                data = date.today()
                if preco <= 15:
                    self.comprar(preco)
                    print("\n############# FIM ##################\n\n\n")
                    return 0
                print('aguardando 30 segundos\n')
                time.sleep(10)

        print('saida do cliente\nvalor: {}\ndata: {}'.format(preco, data))
        print('')
        print("############# FIM ##################")
        print('\n\n\n')

    def comprar(self,preco):
        consusmer_key = ''
        consusmer_secret = ''
        token_key = ''
        token_secret = ''

        consumer = oauth2.Consumer(consusmer_key, consusmer_secret)
        token = oauth2.Token(token_key, token_secret)
        cliente = oauth2.Client(consumer, token)

        pesquisa = 'livro, Web Scraping com PythonWeb Scraping com Python, preço: R$' + str(preco)
        pesquisa_codificada = urllib.parse.quote(pesquisa, safe='')

        requisicao = cliente.request('https://api.twitter.com/1.1/statuses/update.json?status=' + pesquisa_codificada,
                                     method='POST')
        decodificar = requisicao[1].decode()

        objeto = json.loads(decodificar)

        print(objeto)
