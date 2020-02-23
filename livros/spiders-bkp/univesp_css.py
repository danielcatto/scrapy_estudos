import scrapy
import re
import time

class QuotesSpider(scrapy.Spider):
    name = "univespcss"
    start_urls = [
        'https://univesp.br/cursos/engenharia-de-computacao'
    ]

    def parse(self, response):
        url = response.url
        controle_loop = True
        for i in range(1):
            for inscricao in response.css('a.btn::text')[0].re(r'Inscrições Encerradas'):
                print('\n\nEstatus da inscrição: {}\n\n'.format(inscricao))
                self.verifica_metricula(inscricao, url)
            time.sleep(2)

    def verifica_metricula(self, status, url):
        if status != 'Inscrições Encerradas':
            self.publicar_facebook(url)
            print('publicaco')
        else:
            print('aguardando...\n')

