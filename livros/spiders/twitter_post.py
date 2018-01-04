import oauth2
import json
import urllib.parse

consusmer_key = ''
consusmer_secret = ''
token_key = ''
token_secret = ''

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
