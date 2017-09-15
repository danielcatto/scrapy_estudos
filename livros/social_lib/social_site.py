# coding: utf-8

import facebook
import oauth2
import json

class Social():
    def publicar_facebook(self,token, mensagem):
        key_token = token
        graph = facebook.GraphAPI(key_token)
        graph.put_object("me", "feed", message=mensagem)

    def twittar(self, consumer_key, consumer_secret, token_key, token_secret,  mensagem):

        consumer = oauth2.Consumer(consumer_key, consumer_secret)
        token = oauth2.Token(token_key, token_secret)
        cliente = oauth2.Client(consumer, token)
        pesquisa = mensagem
        pesquisa_codificada = pesquisa
        requisicao = cliente.request('https://api.twitter.com/1.1/statuses/update.json?status=' + pesquisa_codificada,
                                     method='POST')
        decodificar = requisicao[1].decode()
        objeto = json.loads(decodificar)
        print(objeto)
