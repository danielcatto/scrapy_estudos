# coding: utf-8

import scrapy
import time
import oauth2
import json
from scrapy.selector import Selector


class QuotesSpider(scrapy.Spider):
    name = "saraiva"
    start_urls = [
        'https://www.saraiva.com.br/programao-em-python-3-uma-introduo-completa-linguagem-python-2858807.html'
    ]


    def parse(self, response):

        sel = Selector(response)
        print("\n\n###################################################\n\n")
        for i in range(10):
            produto = sel.xpath("//h1[@class='livedata']//text()").extract()
            preco = response.css("div.simple-price span.final-price::text").re(r'\w+\,\w+')
            print(produto[0])
            print(preco[0])
            yield {
                'nome': produto[0],
                'preco': preco[0]

                }
            time.sleep(60)

        print("\n\n###################################################")

    def comparar_preco(self, produto, preco_comparativo, preco):
        if (preco <= preco_comparativo):
            desc = ((preco / preco_comparativo) * 100) - 100
            # print('desconto de :', abs(desc))
            if abs(desc) >= 30:
                print('desconto: {:.2f}%'.format(abs(desc)))
                #self.twittar(produto, str(preco))
            else:
                print('1 => sem desconto maior que 30%')

        else:
            print('sem desconto, ou aumento de preço2')

    def para_float(self, preco):
        preco_float = float(preco)
        return preco_float


    def para_converte(self, preco):
        preco_convertido = preco.replace(",", ".")
        return preco_convertido




    def twittar1(self, produto, preco ):
        print('produto: {}, preco: {}'.format(produto, preco))
        print(type(produto))
        print(type(preco))


    def twittar(self,produto, preco):
        consusmer_key = 'yT57HTvtM7drPqQ1fVMtbdsGJ'
        consusmer_secret = 'AYke23tMy9QNMuWpVMD8UTu7MiP8VL2Aee0j7KT8HuEV88uSqZ'
        token_key = '50165680-o7CcGmvB9XmSEdDkWGNNnjUEUNsBXD4vErRMG22k1'
        token_secret = 'zRuIUYEuJfiV7pXQPWkzYgy1a5KODWseIGSoC7iGHJGkU'

        consumer = oauth2.Consumer(consusmer_key, consusmer_secret)
        token = oauth2.Token(token_key, token_secret)
        cliente = oauth2.Client(consumer, token)

        pesquisa = produto + preco
        pesquisa_codificada = pesquisa

        requisicao = cliente.request('https://api.twitter.com/1.1/statuses/update.json?status=' + pesquisa_codificada,
                                     method='POST')
        decodificar = requisicao[1].decode()

        objeto = json.loads(decodificar)

        print(objeto)

