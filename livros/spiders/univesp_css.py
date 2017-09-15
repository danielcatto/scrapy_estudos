import scrapy
import re
import time
import facebook
from social_lib.social_site import Social
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


    def publicar_facebook(self, url):
        token = 'EAACEdEose0cBAA7V5PaZB2HJuV7OtrJpHEnGbxdXpxeAl3LTzKlrKbEvY0CH9Pk3AZA8P1uEhji5XOTtqAgmGsAN5ai6w816TEfkXgxriLKIruqvMipmlD9iII7wZCapzgNb0fyl5gbQxTvKvSefyPJ3z7TZB4VHZAZAYezZAhMYKhSmfcuaxZBvchC6QjzmEg4ZCeXlBnN6EygZDZD'
        graph = facebook.GraphAPI(token)
        graph.put_object("me", "feed", message="Teste de um spider feito para monitorar quando abrirão as inscrições para o vestibular da univesp, em:\n{}".format(url))

