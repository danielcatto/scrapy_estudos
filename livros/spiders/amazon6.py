## coding: utf-8

import scrapy
import time
from datetime import date
#from facepy import GraphAPI
from .facepy.graph_api import GraphAPI
#import oauth2
import json
from scrapy.selector import Selector

class QuotesSpider(scrapy.Spider):
    name = "auto"
    start_urls = [
        'https://www.amazon.com.br/Automatize-Tarefas-Ma%C3%A7antes-com-Python/dp/8575224468/ref=sr_1_1?ie=UTF8&qid=1503414264&sr=8-1&keywords=automatize+tarefas+ma%C3%A7antes+com+python'
    ]


    def parse(self, response):
        controle = True
        sel = Selector(response)
        preco_comparativo = 81.01 #self.para_float(self.para_converte(sel.xpath("//span[@class='a-color-base']//text()").re(r'\w\w\,\w\w')[0]))
        print("\n\n###################################################")

        for i in range(100):
            for produto in sel.xpath("//span[@id='productTitle']//text()").extract():
                preco = sel.xpath("//span[@class='a-color-base']//text()").re(r'\w\w\,\w\w')[0]
                data = date.today()
                url = response.url
                preco_float = self.para_float(self.para_converte(preco))
                yield{
                    'produto': produto, 'preco': preco, 'data': str(data), 'url': url
                }
            self.comparar_preco(produto,preco_comparativo, preco_float, url)
            print('controle', controle)
            print("\n###################################################\n\n")
            print('sleep 3 segundos')
            time.sleep(10)


    def comparar_preco(self, produto, preco_comparativo, preco, url):
        if (preco <= preco_comparativo):
            desc = ((preco / preco_comparativo) * 100) - 100

            if abs(desc) > 30:
                '''
                print('Listar desconto: {:.2f}%'.format(abs(desc)))
                print(preco, preco_comparativo, url)
                #self.twittar1(produto, str(preco),str(preco_comparativo), url, desc)
                '''
                mensagem = 'Livro {},\nPreço: {}\nEndereço {}\nDesconto: {:.2f}%'.format(produto, preco, url, abs(desc))
                print(mensagem)
                self.test_post(mensagem)
                return False
            else:
                print('livro: {}\nPreço {}'.format(produto, preco))
                print('desconto: {:.2f}%'.format(abs(desc)))
                print('Sem desconto%')

                return True
        else:
            print('sem desconto, ou aumento de preço')
            print('livro: {}\nPreço {}'.format(produto, preco))

            return True


    def para_float(self, preco):
        preco_float = float(preco)
        return preco_float


    def para_converte(self, preco):
        preco_convertido = preco.replace(",", ".")
        return preco_convertido

    def test_post(self, mensagem):
        graph = GraphAPI('')
        graph.post(path='me/feed?message='+mensagem)
