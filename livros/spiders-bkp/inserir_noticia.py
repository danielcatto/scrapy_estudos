import _sqlite3
conexao = _sqlite3.connect("dbNoticias.db")
cursor = conexao.cursor()

def gravar(autor, quote, data, url, status):
    cursor.execute('''
            insert into noticia(autor, quote, data, url, status) values(?,?, ?, ?, ?)
            ''', (autor, quote, data, url, status))
    conexao.commit()