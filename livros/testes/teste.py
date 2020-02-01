
import json
import sqlite3
conexao = sqlite3.connect("dbNoticias.db")
cursor = conexao.cursor()

with open('../spiders/aosfatos.json') as f:
    data = json.load(f)

cont = 0
for mat in range(len(data)):
    cursor.execute('''
        insert into noticia(autor, quote, data, url, status) values(?, ?, ?, ?, ?)''',
        (data[mat]['autor'], data[mat]['quote'], data[mat]['data'], data[mat]['url'], data[mat]['status']))
    print('gravado', cont)
    cont+=1
    conexao.commit()

cursor.close()
conexao.close()