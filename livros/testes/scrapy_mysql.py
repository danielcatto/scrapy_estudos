import mysql.connector
import json



with open('../spiders/aosfatos.json') as f:
    data = json.load(f)


mydb = mysql.connector.connect(
  host="192.168.10.162",
  user="root",
  passwd="root",
  database="banco_web2py"
)
print(data[0]['autor'])

count=0
mycursor = mydb.cursor()
for mat in range(len(data)):

    sql = "INSERT INTO news (autor, quote, data, url, status) VALUES (%s, %s, %s, %s, %s)"
    val = (data[mat]['autor'], data[mat]['quote'], data[mat]['data'], data[mat]['url'], data[mat]['status'])
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted. ", count)
    count+=1




'''
MYSQL NO DOCKER
Realizando a baixa da imagem do mysql e configurando um conteiner
>>docker pull mysql
	baixa ultima imagem do mysql 
>>docker run --name banco_web2py -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 -d mysql
	cria o conteiner com os parametro do mysql configurado
>>sudo sudo docker exec -it banco_web2py mysql -p
	para entrar no console do mysql
'''