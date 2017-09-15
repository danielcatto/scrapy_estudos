## coding: utf-8

import scrapy
import time
from datetime import date
import facebook
import oauth2
import json
from scrapy.selector import Selector

class QuotesSpider(scrapy.Spider):
    name = "amazonAutomatize"
    start_urls = [
        'https://www.amazon.com.br/Automatize-Tarefas-Ma%C3%A7antes-com-Python/dp/8575224468/ref=sr_1_1?ie=UTF8&qid=1503414264&sr=8-1&keywords=automatize+tarefas+ma%C3%A7antes+com+python'
    ]


    def parse(self, response):
        controle = True
        sel = Selector(response)
        preco_comparativo = 71  #self.para_float(self.para_converte(sel.xpath("//span[@class='a-color-base']//text()").re(r'\w\w\,\w\w')[0]))
        print("\n\n###################################################")
        for i in range(1):
            for produto in sel.xpath("//span[@id='productTitle']//text()").extract():
                preco = sel.xpath("//span[@class='a-color-base']//text()").re(r'\w\w\,\w\w')[0]
                data = date.today()
                url = response.url
                preco_float = self.para_float(self.para_converte(preco))
                yield{
                    'produto': produto, 'preco': preco, 'data': str(data), 'url': url
                }
                self.comparar_preco(produto,preco_comparativo, preco_float, url)
            print("\n###################################################\n\n")
            time.sleep(3)


    def comparar_preco(self, produto, preco_comparativo, preco, url):
        if (preco <= preco_comparativo):
            desc = ((preco / preco_comparativo) * 100) - 100
            if abs(desc) >= 30:
                print('desconto: {:.2f}%'.format(abs(desc)))
                self.twittar1(produto, str(preco),str(preco_comparativo), url, desc)
                self.publicar_facebook(self, produto, preco, preco_comparativo, url, desc)
            else:
                print('livro: {}\nPreço {}'.format(produto, preco))
                print('desconto: {:.2f}%'.format(abs(desc)))
                print('Sem desconto maior que 30%')
        else:
            print('sem desconto, ou aumento de preço2')


    def para_float(self, preco):
        preco_float = float(preco)
        return preco_float


    def para_converte(self, preco):
        preco_convertido = preco.replace(",", ".")
        return preco_convertido


    def publicar_facebook(self, produto, preco, preco_comparativo, url, desconto):
        token = 'EAACEdEose0cBAA7V5PaZB2HJuV7OtrJpHEnGbxdXpxeAl3LTzKlrKbEvY0CH9Pk3AZA8P1uEhji5XOTtqAgmGsAN5ai6w816TEfkXgxriLKIruqvMipmlD9iII7wZCapzgNb0fyl5gbQxTvKvSefyPJ3z7TZB4VHZAZAYezZAhMYKhSmfcuaxZBvchC6QjzmEg4ZCeXlBnN6EygZDZD'
        graph = facebook.GraphAPI(token)
        graph.put_object("me", "feed", message="Livro: {} está com desconto de {}\npreco:{}\npreço anterior{}\nurl: {}".format(produto, desconto,preco, preco_comparativo, url))


    def twittar1(self, produto, preco, preco_comparativo, url, desconto):
        print('\n\nTwitar isso\nproduto: {}\nde: {} por: {}\nurl {}\ndesconto {}'.format(produto, preco_comparativo, preco, url, desconto))


    def twittar(self, produto, preco, preco_comparativo, url, desconto):
        consusmer_key = 'yT57HTvtM7drPqQ1fVMtbdsGJ'
        consusmer_secret = 'AYke23tMy9QNMuWpVMD8UTu7MiP8VL2Aee0j7KT8HuEV88uSqZ'
        token_key = '50165680-o7CcGmvB9XmSEdDkWGNNnjUEUNsBXD4vErRMG22k1'
        token_secret = 'zRuIUYEuJfiV7pXQPWkzYgy1a5KODWseIGSoC7iGHJGkU'
        consumer = oauth2.Consumer(consusmer_key, consusmer_secret)
        token = oauth2.Token(token_key, token_secret)
        cliente = oauth2.Client(consumer, token)
        pesquisa = 'Twitar isso\nproduto: {}\npreco: {}\nurl {}\ndesconto {}'.format(produto, preco, url, desconto)
        pesquisa_codificada = pesquisa
        requisicao = cliente.request('https://api.twitter.com/1.1/statuses/update.json?status=' + pesquisa_codificada,
                                     method='POST')
        decodificar = requisicao[1].decode()
        objeto = json.loads(decodificar)
        print(objeto)
