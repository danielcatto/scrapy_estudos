import oauth2
import urllib.parse
import json

class Twitter:
    def __init__(self, consumer_key, consumer_secret, token_key, token_secret):
        self.conexao(consumer_key, consumer_secret, token_key, token_secret)


    def conexao(self, consumer_key, consumer_secret, token_key, token_secret):

        self.consumer = oauth2.Consumer(consumer_key, consumer_secret)
        self.token = oauth2.Token(token_key, token_secret)
        self.cliente = oauth2.Client(self.consumer, self.token)

    def tweet(self, novo_twitter):
        pesquisa_codificada = urllib.parse.quote(novo_twitter, safe='')
        requisicao = self.cliente.request('https://api.twitter.com/1.1/statuses/update.json?status=' + pesquisa_codificada,
                                     method='POST')
        decodificar = requisicao[1].decode()
        objeto = json.loads(decodificar)
        return objeto

    def statos(self):
        pesquisa = input("Informe um assunto")
        pesquisa_codificada = urllib.parse.quote(pesquisa, safe='')

        requisicao = self.cliente.request(
            'https://api.twitter.com/1.1/search/tweets.json?q=' + pesquisa_codificada + '&lang=pt')
        decodificar = requisicao[1].decode()

        objeto = json.loads(decodificar)

        arq = open('arquivo.txt', 'a')
        arq.writelines(str(objeto['statuses'][1]['user']['screen_name'] + '\n'))

        twittes = objeto['statuses']

        for twit in twittes:
            print(twit['text'])
            print(twit['user']['screen_name'])
            arq.writelines(twit['text'])
            arq.writelines(twit['user']['screen_name'])

'''
consumer_key = 'yT57HTvtM7drPqQ1fVMtbdsGJ'
consumer_secret = 'AYke23tMy9QNMuWpVMD8UTu7MiP8VL2Aee0j7KT8HuEV88uSqZ'
token_key =	'50165680-o7CcGmvB9XmSEdDkWGNNnjUEUNsBXD4vErRMG22k1'
token_secret	= 'zRuIUYEuJfiV7pXQPWkzYgy1a5KODWseIGSoC7iGHJGkU'


t = Twitter(consumer_key, consumer_secret, token_key,token_secret)


print(t.statos())
'''