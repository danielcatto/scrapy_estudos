import oauth2
import json
import urllib.parse

consusmer_key = 'yT57HTvtM7drPqQ1fVMtbdsGJ'
consusmer_secret = 'AYke23tMy9QNMuWpVMD8UTu7MiP8VL2Aee0j7KT8HuEV88uSqZ'
token_key = '50165680-o7CcGmvB9XmSEdDkWGNNnjUEUNsBXD4vErRMG22k1'
token_secret = 'zRuIUYEuJfiV7pXQPWkzYgy1a5KODWseIGSoC7iGHJGkU'

consumer = oauth2.Consumer(consusmer_key, consusmer_secret)
token = oauth2.Token(token_key, token_secret)
cliente = oauth2.Client(consumer, token)

pesquisa = ':D'
pesquisa_codificada = urllib.parse.quote(pesquisa, safe='')

requisicao = cliente.request('https://api.twitter.com/1.1/statuses/update.json?status=' + pesquisa_codificada,
                             method='POST')
decodificar = requisicao[1].decode()

objeto = json.loads(decodificar)

print(objeto)